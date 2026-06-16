# Travel Item Control Character Guard

status: completed

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

## Work Completed

- Rejected normalized names containing Unicode control characters at the
  shared model boundary used by both UI and direct collection callers.
- Added focused XCTest intent for newline, tab, and NUL rejection while
  preserving an accented display name.
- Extended the deterministic checker and maintained repository guidance with
  mutation-sensitive contracts for the new boundary.

## Verification Completed

- All four Make gates passed from the checkout and reported that `xcodebuild`
  was unavailable, so this Linux host exercised the complete static baseline.
- The absolute Makefile path passed the full gate from an external directory.
- `python3 -m py_compile scripts/check-baseline.py` and `git diff --check`
  passed with plist, storyboard, workspace, project, asset, and workflow
  parsing retained by the baseline.
- Six isolated hostile mutations were rejected for source-guard removal,
  newline and NUL regression removal, internationalized-name preservation
  removal, maintained-guidance removal, and completed-plan status rollback.
- Exact intended-file, generated-artifact, file-mode, conflict-marker, and
  credential-pattern audits passed before commit.
