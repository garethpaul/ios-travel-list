# Changes

## 2026-06-08

- Trimmed new travel item names before accepting them so whitespace-only entries are ignored.
- Avoided force-unwrapping travel item text and reset pending items before each add segue.
- Guarded storyboard/table cell casts and invalid delete indexes.
- Rejected partial invalid hex color scans so malformed colors fall back to gray.
- Removed table reload work from cell rendering.
- Added `make check` and a static Swift/Xcode baseline for plist/storyboard/asset metadata, source inventory, list-flow guardrails, and local-first privacy checks.
- Documented the legacy Xcode project, local-first list behavior, and static verification workflow.
