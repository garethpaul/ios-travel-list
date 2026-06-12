# XCTest Target Build

status: completed

## Context

The repository contains focused Swift XCTest source and a test-bundle plist,
but `TravelList.xcodeproj` has no `TravelListTests` native target. Hosted CI
therefore compiles only the app and cannot detect compiler regressions in the
normalization and guarded-removal tests.

## Completed Scope

- Add a `TravelListTests` unit-test bundle target using the checked-in test
  source and plist.
- Link the test target to the app through a target dependency and test host.
- Keep iOS 12 and Swift 5 settings aligned across app and test targets.
- Compile both the app and XCTest target through `build.sh` and `make check`.
- Extend the static baseline and documentation with the executable-test-target
  contract.
- Mutation-test removal of the test target, source phase, dependency, and build
  invocation.

## Verification

- `make lint`
- `make test`
- `make build`
- `make check`
- `python3 -m py_compile scripts/check-baseline.py`
- hosted unsigned app and XCTest target compilation
- `git diff --check`
- Mutation results: removing the unit-test product type, test source membership,
  app target dependency, or `build.sh` test-target invocation was rejected by
  `scripts/check-baseline.py`.
