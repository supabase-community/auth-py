# Changelog

<!--next-version-placeholder-->

## v0.5.4 (2022-08-31)
### Fix
* Use `str` type instead of `UUID` type in `id` property of `Identity` model ([#156](https://github.com/supabase-community/gotrue-py/pull/156)) thanks to [@leynier](https://github.com/leynier)

## v0.5.3 (2022-07-16)
### Fix
* Set total false to user attributes typed dict

## v0.5.2 (2022-07-13)
### Feature
* Change .update method to also allow dictionaries ([#130](https://github.com/supabase-community/gotrue-py/pull/130)) thanks to [@odiseo0](https://github.com/odiseo0)

## v0.5.1 (2022-07-04)
### Fix
* Upgrade dependencies and fix config tests ([#126](https://github.com/supabase-community/gotrue-py/pull/126))

## v0.5.0 (2022-01-20)
### Feature
* Add create user param to sign in ([#75](https://github.com/supabase-community/gotrue-py/issues/75)) ([`57ec6d8`](https://github.com/supabase-community/gotrue-py/commit/57ec6d8efe1233c1b90a8585045e6f85a4a3c17b))

### Documentation
* Add maintainers file ([`2f5f005`](https://github.com/supabase-community/gotrue-py/commit/2f5f005235e90127cb7effde7396bb55088b815f))

**[See all commits in this version](https://github.com/supabase-community/gotrue-py/compare/v0.4.0...v0.5.0)**

## v0.4.0 (2022-01-17)
### Feature
* Add notion to enum of providers ([#70](https://github.com/supabase-community/gotrue-py/issues/70)) ([`a8f2c45`](https://github.com/supabase-community/gotrue-py/commit/a8f2c45b25c9d008de7a5e1e6f18cc47a259c73c))

**[See all commits in this version](https://github.com/supabase-community/gotrue-py/compare/v0.3.5...v0.4.0)**

## v0.3.5 (2022-01-15)
### Fix
* Delete_user returns Exception event if response is Ok ([#68](https://github.com/supabase-community/gotrue-py/issues/68)) ([`23c167e`](https://github.com/supabase-community/gotrue-py/commit/23c167e7082c5ddb4dd64b958aa55065c2b3e468))

**[See all commits in this version](https://github.com/supabase-community/gotrue-py/compare/v0.3.4...v0.3.5)**

## v0.3.4 (2022-01-13)
### Fix
* String formatting in `delete_user` ([#64](https://github.com/supabase-community/gotrue-py/issues/64)) ([`d783015`](https://github.com/supabase-community/gotrue-py/commit/d783015b5d2472fe95a83f5d42efe97f79331516))

**[See all commits in this version](https://github.com/supabase-community/gotrue-py/compare/v0.3.3...v0.3.4)**

## v0.3.3 (2022-01-08)

**[See all commits in this version](https://github.com/supabase-community/gotrue-py/compare/v0.3.2...v0.3.3)**

## v0.3.2 (2022-01-04)
### Fix
* Deploy action ([`467fa3f`](https://github.com/supabase-community/gotrue-py/commit/467fa3f6b9e09295806cbac3e8c4fcfe05c3147d))

**[See all commits in this version](https://github.com/supabase-community/gotrue-py/compare/v0.3.1...v0.3.2)**

## v0.3.0 (2021-12-03)

### Fix

* error in get_session_from_url
* add a new TOKEN_REFRESHED event
* get recovery mode before notify sign in event
* remove duplicate var env in docker-compose.yml
* use str for declare Python 3.10
* use expires_in var for avoid typing warning
* use typing annotations
* use directly parse_obj instead of lambdas
* use parse_obj
* set prefix __ instead of _ for private methods
* .pre-commit-config.yaml format
* change Api by API
* change ApiError by APIError in docstrings
* change ApiError by APIError
* add Optional to identities of User
* add slack adn spotify to Provider
* remove Optional to user_metadata of User
* remove email_change_confirm_status from User
* some fixes and changes requested
* some tipe hints
* error in client update
* errors in helpers and types
* ci github action
* remove unnecessary async to on_auth_state_change
* error in remove_item of memory storage
* cycle of references between helpers and types
* use environ vars only if present
* reinstate lib **init**.py
* reinstate lib.constants
* readjust indent in ci.yml

### Feat

* add job to github action for auto deploy
* add pre-commit hook for conventional commit
* add devcontainer.json for use github codespaces
* add X-Client-Info to default headers
* allow providing custom api and http client implementation
* add create_user and list_users
* add datetime and uuid types
* add pyupgrade pre-commit hook
* migrate types to pydantic models
* unify logic of __recover_session and__recover_and_refresh
* uuid4().hex instead of str(uuid4()) in _sync client
* uuid4().hex instead of str(uuid4())
* add --ignore-init-module-imports to .pre-commit-config.yaml
* add end-of-file-fixer to .pre-commit-config.yaml
* use asdict of dataclasses for to_dicts
* use annotations from **future**
* add identities to User
* use reflection for parsing dataclasses
* implement and use cli for unasync
* force the use of keyword parameters
* generate tests for sync client
* add Make rule for infra
* add pre-commit system for check Pythonic style
* add context manager support
* implement sync/async support with httppx and unasync
* add poetry to CI action and add dependabot config file
* synchronize implementation of GoTrueClient
* add CookieOptions to constructor of GoTrueApi
* implement SupportedStorage abstract storage and MemoryStorage storage
* implement Subscription type
* implement AuthChangeEvent enum
* implement CookieOptions type
* add types to API class and align implementation with gotrue-js
* add new types, implement to_dicts and align files with gotrue-js
* implement dataclasses with methods for parsing
