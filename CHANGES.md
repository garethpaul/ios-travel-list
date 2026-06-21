# Changes

## 2026-06-21

- Aligned target-local app and XCTest bundle identifiers with their existing
  Info.plist identifiers and added a static mismatch regression contract.

## 2026-06-19

- Collapsed accepted horizontal Unicode whitespace to ordinary spaces and used
  a fixed-locale case- and width-insensitive duplicate key for new and existing
  travel item names.
- Added simulator XCTest coverage and five mutation-sensitive baseline checks
  for the corrected canonicalization boundary.

## 2026-06-17

- Rejected embedded Unicode line separators at the shared travel-item name
  boundary and added focused XCTest coverage.

## 2026-06-16

- Rejected embedded control characters at the shared travel-item name boundary
  while preserving ordinary internationalized display names.

## 2026-06-15

- Normalized existing item names during duplicate checks so legacy or direct
  noncanonical rows cannot admit an equivalent canonical item.

## 2026-06-14

- Canonicalized direct travel-item additions before duplicate comparison and
  rejected blank names at the collection mutation boundary.

## 2026-06-13

- Made all Make verification aliases location-independent when invoked through
  an absolute Makefile path.
- Added case-insensitive duplicate item checks before user-added list mutation
  and table reload.

## 2026-06-12

- Added an app-hosted `TravelListTests` target and made `make check` compile the
  unsigned app and XCTest bundle together.

## 2026-06-10

- Migrated the app and checked-in test source to Swift 5 and iOS 12.
- Replaced `NSMutableArray` list storage with typed `[TravelListItem]` storage.
- Added an unsigned simulator app build to `make check` and hosted macOS CI.
- Guarded add-screen textfield outlet reads so missing storyboard wiring falls
  back through the shared name normalizer.
- Added pinned, read-only macOS GitHub Actions project validation for
  `make check` and `TravelList.xcodeproj` parsing without persisted checkout
  credentials.

## 2026-06-09

- Added local `make lint`, `make test`, and `make build` gate aliases for the
  static Travel List baseline.
- Added a removal index guard so invalid travel item selections do not mutate
  the local list.
- Scoped the travel logo to each navigation item title view instead of adding
  navigation-controller overlay subviews.

## 2026-06-08

- Trimmed new travel item names before accepting them so whitespace-only entries are ignored.
- Moved travel item trimming into a shared name normalizer on the model.
- Replaced generated test placeholders with normalizer tests for trimmed, blank, and missing item names.
- Avoided force-unwrapping travel item text and reset pending items before each add segue.
- Guarded storyboard/table cell casts and invalid delete indexes.
- Guarded table cell indexes before reading list data during rendering.
- Switched cell rendering to a configurable fallback cell when storyboard reuse wiring is unavailable.
- Cleared stale cell text and accessory state before returning fallback cells for invalid or malformed rows.
- Rejected partial invalid hex color scans so malformed colors fall back to gray.
- Removed table reload work from cell rendering.
- Added `make check` and a static Swift/Xcode baseline for plist/storyboard/asset metadata, source inventory, list-flow guardrails, and local-first privacy checks.
- Documented the legacy Xcode project, local-first list behavior, and static verification workflow.
