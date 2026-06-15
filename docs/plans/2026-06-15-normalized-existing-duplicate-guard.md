# Normalized Existing Duplicate Guard

status: completed

## Context

`addTravelItem` normalizes the incoming name before comparison, but compares it
against each existing item's raw stored name. A preexisting noncanonical item
such as `" Passport "` can therefore admit a duplicate canonical `"Passport"`
row even though the collection boundary is intended to reject equivalent names.

## Requirements

- Normalize both the candidate and each existing item name before duplicate
  comparison.
- Reject case-insensitive canonical duplicates without mutating either item or
  the collection.
- Preserve canonical storage for successful additions, blank rejection,
  unwind behavior, seeded data, removal behavior, storyboard wiring, and local
  storage.
- Add focused XCTest and mutation-sensitive static coverage for a noncanonical
  existing item.

## Implementation

- Compare the normalized candidate against normalized existing names inside
  the shared collection mutation boundary.
- Add an XCTest that seeds a padded existing item and rejects an equivalent
  canonical candidate without changing either value or the collection count.
- Extend the deterministic checker to require the implementation, focused
  test, plan completion evidence, and intended documentation updates.

## Verification

- Run the focused checker and all four Make gates from the checkout.
- Run the full gate through the absolute Makefile path from an external working
  directory.
- Compile the checker and validate shell, project, plist, storyboard, asset,
  and workflow metadata where supported.
- Reject isolated mutations that remove existing-name normalization, weaken
  the focused test, or falsify completed plan evidence.
- Audit the exact diff, generated artifacts, and intended files for secret
  patterns before committing.

## Work Completed

- Normalized existing item names before case-insensitive duplicate comparison
  while preserving their stored display text.
- Added focused XCTest and static contracts for padded existing-item names.
- Recorded the behavior change in the changelog.

## Verification Completed

- All four Make gates passed from the checkout and reported that `xcodebuild` was unavailable,
  so this Linux host exercised the complete static baseline.
- The full gate passed from an external directory through the absolute Makefile path.
- `python3 -m py_compile scripts/check-baseline.py`, `sh -n build.sh`, plist,
  storyboard, workspace, project, asset, and workflow parsing, and
  `git diff --check` passed.
- Five isolated hostile mutations were rejected: missing existing-name
  normalization, raw existing-name comparison, missing focused test discovery,
  unfinished plan status, and weakened mutation evidence.
- Exact intended-file generated-artifact and secret-pattern audits passed.
- Hosted macOS app and XCTest-target compilation is recorded separately after
  push; this plan claims only completed local evidence.
