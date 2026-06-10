# Changes

## 2026-06-10

- Guarded add-screen textfield outlet reads so missing storyboard wiring falls
  back through the shared name normalizer.
- Added pinned, read-only macOS hosted project validation for `make check` and
  `TravelList.xcodeproj` parsing.

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
