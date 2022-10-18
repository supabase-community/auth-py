from typing import AsyncIterable

import pytest
from faker import Faker

from ...gotrue import AsyncGoTrueClient
from ...gotrue.errors import APIError
from ...gotrue.types import User

GOTRUE_URL = "http://localhost:9999"
TEST_TWILIO = False


@pytest.fixture(name="client")
async def create_client() -> AsyncIterable[AsyncGoTrueClient]:
    async with AsyncGoTrueClient(
        url=GOTRUE_URL,
        auto_refresh_token=False,
        persist_session=False,
    ) as client:
        yield client


fake = Faker()

email = fake.email().lower()
password = fake.password()
phone = fake.phone_number()  # set test number here


async def test_sign_up_with_email_and_password(client: AsyncGoTrueClient):
    try:
        response = await client.sign_up(
            email=email,
            password=password,
            data={"status": "alpha"},
        )
        assert isinstance(response, User)
        assert not response.email_confirmed_at
        assert not response.last_sign_in_at
        assert response.email == email
    except Exception as e:
        assert False, str(e)


@pytest.mark.depends(on=[test_sign_up_with_email_and_password.__name__])
async def test_sign_up_with_the_same_user_twice_should_throw_an_error(
    client: AsyncGoTrueClient,
):
    expected_error_message = "For security purposes, you can only request this after"
    try:
        await client.sign_up(
            email=email,
            password=password,
        )
        assert False
    except APIError as e:
        assert expected_error_message in e.msg
    except Exception as e:
        assert False, str(e)


@pytest.mark.depends(on=[test_sign_up_with_email_and_password.__name__])
async def test_sign_in(client: AsyncGoTrueClient):
    expected_error_message = "Email not confirmed"
    try:
        await client.sign_in(
            email=email,
            password=password,
        )
        assert False
    except APIError as e:
        assert e.msg == expected_error_message
    except Exception as e:
        assert False, str(e)


@pytest.mark.depends(on=[test_sign_up_with_email_and_password.__name__])
async def test_sign_in_with_the_wrong_password(client: AsyncGoTrueClient):
    expected_error_message = "Invalid login credentials"
    try:
        await client.sign_in(email=email, password=f"{password}2")
        assert False
    except APIError as e:
        assert e.msg == expected_error_message
    except Exception as e:
        assert False, str(e)


@pytest.mark.skipif(not TEST_TWILIO, reason="Twilio is not available")
async def test_sign_up_with_phone_and_password(client: AsyncGoTrueClient):
    try:
        response = await client.sign_up(
            phone=phone,
            password=password,
            data={"status": "alpha"},
        )
        assert isinstance(response, User)
        assert not response.phone_confirmed_at
        assert not response.email_confirmed_at
        assert not response.last_sign_in_at
        assert response.phone == phone
    except Exception as e:
        assert False, str(e)


@pytest.mark.skipif(not TEST_TWILIO, reason="Twilio is not available")
@pytest.mark.depends(on=[test_sign_up_with_phone_and_password.__name__])
async def test_verify_mobile_otp_errors_on_bad_token(client: AsyncGoTrueClient):
    expected_error_message = "Otp has expired or is invalid"
    try:
        await client.verify_otp(phone=phone, token="123456")
        assert False
    except APIError as e:
        assert expected_error_message in e.msg
    except Exception as e:
        assert False, str(e)
