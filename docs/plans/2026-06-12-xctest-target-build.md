# XCTest Target Build

status: completed

## Context

The repository contains focused Swift XCTest source and a test-bundle plist,
but `TravelList.xcodeproj` has no `TravelListTests` native target. Hosted CI
therefore compiles only the app and cannot detect compiler regressions in the
normalization and guarded-removal tests.

## Work Completed

- Add a `TravelListTests` unit-test bundle target using the checked-in test
  source and plist.
- Link the test target to the app through a target dependency and test host.
- Keep iOS 12 and Swift 5 settings aligned across app and test targets.
- Compile both the app and XCTest target through `build.sh` and `make check`.
- Extend the static baseline and documentation with the executable-test-target
  contract.
- Mutation-test removal of the test target, source phase, dependency, and build
  invocation.

## Verification Completed

- Local `make check`, `make lint`, `make test`, and `make build` passed. The
  local environment did not provide `xcodebuild`, so `build.sh` reported the
  hosted Xcode requirement after the complete static baseline passed.
- `python3 -m py_compile scripts/check-baseline.py`, `sh -n build.sh`, and
  `git diff --check` passed.
- Hostile mutations changing the plan status, inserting an unfinished-work
  marker, falsifying a run ID, removing the unit-test product type, or removing
  the `build.sh` test-target invocation were rejected.
- The implementation push Check run `27395471515` completed successfully for
  commit `6e6727a004a980f958bf039baf33c306720378df`.
- The implementation pull-request Check run `27395475871` completed
  successfully for commit `6e6727a004a980f958bf039baf33c306720378df` and
  compiled the unsigned app and XCTest target on hosted macOS.
- The post-merge push Check run `27395516880` completed successfully for
  commit `ce8e091b3182eb82840a33e85940d0d5657685f8`.
- The CodeQL setup run `27402323830` completed successfully for commit
  `ce8e091b3182eb82840a33e85940d0d5657685f8`.
- The project preserves `com.apple.product-type.bundle.unit-test`,
  `TravelListTests.swift in Sources`, the TravelList target dependency, and
  `-target "TravelListTests"` in `build.sh`.
