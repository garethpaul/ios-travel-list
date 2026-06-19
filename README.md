# ios-travel-list

<!-- README-OVERVIEW-IMAGE -->
![Project overview](docs/readme-overview.svg)

## Overview

`garethpaul/ios-travel-list` is an Apple platform application or Swift sample. Travel List so you don't forget things.

This README is based on the checked-in source, manifests, scripts, and repository metadata on the `master` branch. The project language mix found during review was: Swift (6), C/C++ headers (1).

## Repository Contents

- `CHANGES.md` - concise history of maintenance changes
- `Makefile` - local verification entry point
- `README.md` - project overview and local usage notes
- `SECURITY.md` - security reporting and disclosure guidance
- `scripts/check-baseline.py` - static Swift/Xcode list-flow verifier
- `TravelList` - source or example code
- `TravelList.xcodeproj` - Xcode project file
- `TravelListTests` - source or example code
- `VISION.md` - project direction and maintenance guardrails

Additional scan context:

- Source directories: TravelList, TravelListTests
- Dependency and build manifests: none detected
- Entry points or build surfaces: `make lint`, `make test`, `make build`, `make check`, TravelList.xcodeproj
- Test-looking files: TravelListTests/Info.plist, TravelListTests/TravelListTests.swift

## Getting Started

### Prerequisites

- Git
- macOS with Xcode for building Apple platform projects
- Python 3 for local static verification on non-macOS hosts

### Setup

```bash
git clone https://github.com/garethpaul/ios-travel-list.git
cd ios-travel-list
make lint
make test
make build
make check
```

The checked-in project has no external dependency manifest. Use Xcode for full builds and the local Make gates for static verification on hosts without Xcode.

## Running or Using the Project

- Open `TravelList.xcodeproj` in Xcode, choose the app or sample scheme, and run it on the matching simulator/device.
- Run `./build.sh` to compile the unsigned Swift 5 app for the simulator when
  Xcode is installed.
- The sample is local-first and keeps list items in memory.
- New item names go through a shared name normalizer at both UI creation and the collection add boundary; whitespace-only entries are ignored and accepted Unicode horizontal whitespace runs are stored as one ordinary space.
- Add-screen textfield outlet reads fall back through the same normalizer when the outlet is unavailable.
- Focused normalizer tests cover trimmed, blank, missing, control-character,
  Unicode line separator, and horizontal Unicode whitespace travel item names.
- Cell rendering uses a fallback cell that can still display an item if storyboard reuse wiring is unavailable.
- Invalid or malformed rows clear stale cell text and accessory state before the fallback cell is returned.
- Item removal index checks reject stale or invalid row selections before mutating the local list.
- Duplicate item checks use a fixed-locale case- and width-insensitive key for
  both new and existing names before appending or reloading the table.
- The travel logo is scoped to each navigation item title view instead of being
  added as a navigation-controller overlay.

## Testing and Verification

Run the local static baseline:

```bash
make lint
make test
make build
make check
```

Each Make gate runs `scripts/check-baseline.py` plus five hostile canonicalization mutations, parses plist/storyboard/asset metadata, checks image resources and Xcode wiring, verifies typed travel-item storage, the shared name normalizer and its embedded control-character guard, rejects Unicode line separators, canonicalizes horizontal Unicode whitespace, checks the fixed-locale case/width duplicate key, guarded textfield outlet reads, focused XCTest source, navigation logo title view ownership, fallback cell reset, table/removal index guards, invalid color fallback, and side-effect-free cell rendering, and guards against logging, network, upload, analytics, or persistence behavior. When Xcode is available the same gate compiles the unsigned app and XCTest target; otherwise the build step skips cleanly.

Pinned `macos-15` GitHub Actions runs `make check` and compiles the unsigned
Swift 5 app and XCTest target. This hosted validation does not inspect travel-item data,
execute simulator interaction, or use signing material.

The checked-in XCTest source is attached to `TravelListTests`; the hosted gate
compiler-checks its assertions without launching a simulator test session.

When the required SDK or runtime is unavailable, use static checks and source review first, then verify on a machine that has the matching platform toolchain.

## Configuration and Secrets

- No required secret or credential file was identified in the repository scan. If you add integrations later, keep secrets out of git.

## Security and Privacy Notes

- Review changes touching network requests, sockets, or service endpoints; examples from the scan include TravelList/Info.plist, TravelListTests/Info.plist.
- Review changes touching file, media, JSON, XML, CSV, OCR, or data parsing; examples from the scan include TravelList/AddTravelViewController.swift, TravelList/Info.plist, TravelList/TravelListTableViewController.swift, TravelListTests/Info.plist.
- Travel lists can reveal personal plans. Keep list data local-first unless a future change documents storage, sync, consent, and deletion behavior.
- Cell rendering should remain side-effect free and validate row indexes before reading list data; avoid reloading the table from inside `cellForRowAtIndexPath`.
- Keep fallback cell handling configurable so valid rows can still display item text if storyboard reuse wiring changes.
- Clear stale cell text and accessory state before returning fallback cells for invalid or malformed rows.
- Keep storyboard casts, text-field reads, table indexes, and color parsing guarded so malformed local UI state falls back safely.

## Maintenance Notes

- This looks like an Apple platform project or sample. Xcode, Swift, CocoaPods, and deployment target versions may need to match the original project era.
- See `SECURITY.md` for vulnerability reporting and safe research guidance.
- See `VISION.md` for project direction and contribution guardrails.
- See `docs/plans/2026-06-09-travel-item-name-normalizer.md` for the shared name normalizer guardrail.
- See `docs/plans/2026-06-09-travel-item-normalizer-tests.md` for the normalizer tests guardrail.
- See `docs/plans/2026-06-09-travel-item-removal-index-guard.md` for the removal index guardrail.
- See `docs/plans/2026-06-13-duplicate-travel-item-guard.md` for the duplicate
  item guardrail.
- See `docs/plans/2026-06-14-canonical-travel-item-add-boundary.md` for direct
  caller normalization at the collection mutation boundary.
- See `docs/plans/2026-06-16-travel-item-control-character-guard.md` for the
  embedded control-character boundary.
- See `docs/plans/2026-06-17-020-reject-unicode-line-separators-plan.md` for the
  Unicode line separator boundary.
- See `docs/plans/2026-06-09-navigation-logo-title-view.md` for the navigation logo title view guardrail.
- See `docs/plans/2026-06-10-add-textfield-outlet-guard.md` for the textfield outlet guardrail.
- See `docs/plans/2026-06-09-make-gate-aliases.md` for the local gate alias guardrail.
- See `docs/plans/2026-06-10-ci-baseline.md` for the GitHub Actions static
  baseline.
- See `docs/plans/2026-06-10-hosted-project-validation.md` for pinned macOS
  project parsing and unsigned build validation.
- See `docs/plans/2026-06-10-swift-5-typed-list-build.md` for the Swift 5 typed
  list migration and current XCTest target limitation.
- Run `make lint`, `make test`, `make build`, and `make check` before pushing changes to Swift sources, plist/storyboard files, image assets, Xcode metadata, list flow, or privacy documentation.
- The same gates may be invoked through an absolute Makefile path from another
  directory; verification resolves both commands relative to the checkout.

## Contributing

Keep changes small and tied to the project that is already present in this repository. For code changes, document the toolchain used, avoid committing generated dependency directories or local configuration, and update this README when setup or verification steps change.
