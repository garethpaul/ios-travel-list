# Swift 5 Typed List Build

status: completed

## Problem

The app and test source use Swift 2-era APIs and an Objective-C mutable array,
while the project targets iOS 8 and hosted validation only parses project
metadata. The checked-in XCTest source is not attached to an XCTest target.

## Scope

- Migrate app and test source to Swift 5 and current UIKit/Foundation APIs.
- Replace `NSMutableArray` with `[TravelListItem]` while preserving index guards,
  normalization, seed items, and fallback-cell reset behavior.
- Raise project and app configurations to iOS 12 and Swift 5.
- Add an unsigned simulator app build to the canonical `make check` gate.
- Extend the static baseline to guard typed storage and modern build settings.
- Document that checked-in XCTest source remains non-executable until a test
  target is added in a dedicated project-structure change.

## Verification

- `make lint`
- `make test`
- `make build`
- `make check`
- hosted unsigned `TravelList` target build
- mutation checks for typed storage and compiler-gate regressions
- `git diff --check`
