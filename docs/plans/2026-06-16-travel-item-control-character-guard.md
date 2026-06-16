# Travel Item Control Character Guard

status: planned

## Context

`TravelListItem.normalizedName` trims whitespace and rejects empty input, but
still accepts embedded control characters. A direct caller can therefore add a
name containing a newline, carriage return, tab, NUL, or another control scalar
that renders as a malformed, multi-line, or invisible table row.

## Requirements

- Reject normalized travel-item names containing Unicode control characters.
- Continue trimming surrounding whitespace and newlines before validation.
- Preserve ordinary punctuation, spaces, and non-ASCII display names.
- Keep successful canonical storage, case-insensitive duplicate rejection,
  seeded data, removal behavior, storyboard wiring, and the no-persistence
  sample boundary unchanged.
- Add focused XCTest and mutation-sensitive static coverage for embedded
  control characters and an ordinary internationalized name.

## Implementation

- Extend the shared model normalizer in `TravelList/TravelListItem.swift` so
  every UI and direct-call path receives the same control-character boundary.
- Add focused cases in `TravelListTests/TravelListTests.swift` for embedded
  newline, tab, and NUL rejection plus preservation of an accented name.
- Extend `scripts/check-baseline.py` to protect the source boundary, focused
  tests, maintained guidance, and completed plan evidence.
- Update `README.md`, `SECURITY.md`, `VISION.md`, and `CHANGES.md` with the
  user-visible and verification contract.

## Verification

- Run all four Make gates and the absolute Makefile gate from an external
  directory.
- Compile the deterministic checker and validate shell, plist, storyboard,
  project, asset, workspace, and workflow metadata where supported.
- Reject isolated mutations that remove the source guard, weaken the focused
  rejection or preservation cases, remove maintained guidance, or falsify the
  plan status.
- Audit the exact intended diff, generated artifacts, file modes, conflict
  markers, and credential-like additions before committing.

## Runtime Boundary

The Linux environment cannot execute Xcode or XCTest. Local verification will
truthfully cover the deterministic static baseline; hosted macOS compilation
evidence will be recorded separately after push.
