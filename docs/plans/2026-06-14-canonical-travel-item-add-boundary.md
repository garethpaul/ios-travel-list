# Canonical Travel Item Add Boundary

status: completed

## Context

The add screen normalizes names before constructing a travel item, but the
shared `addTravelItem` helper accepts any direct `TravelListItem`. A non-UI
caller can therefore add blank names or whitespace-padded duplicates such as
`" Passport "` beside the existing `"Passport"` row.

## Requirements

- Normalize every candidate name inside `addTravelItem` before duplicate
  comparison or list mutation.
- Reject missing, blank, and whitespace-only canonical names without changing
  the list.
- Compare duplicates case-insensitively and store the normalized display name
  on successful append.
- Preserve the unwind flow, reload-on-success behavior, seeded items, removal
  semantics, storyboard wiring, layout, and local-only storage.
- Add focused XCTest cases and mutation-sensitive static contracts.

## Implementation

- Guard `TravelListItem.normalizedName(item.itemName)` at the collection
  mutation boundary and assign the canonical result before appending.
- Extend unit coverage for padded unique names, padded case variants, and blank
  direct callers.
- Synchronize the static checker and contributor documentation with completed
  verification evidence.

## Verification

- Run the focused baseline and all four Make gates from the checkout.
- Run the full gate through an absolute Makefile path from an external working
  directory.
- Compile the checker and validate shell, plist, storyboard, project, asset,
  and workflow metadata where supported.
- Reject hostile mutations for missing normalization, storing raw input,
  duplicate comparison before canonicalization, missing focused tests, stale
  plan status, and missing verification evidence.
- Audit the exact diff, generated artifacts, and intended files for secret
  patterns before committing.

## Work Completed

- Normalized names inside `addTravelItem` before duplicate comparison and list
  mutation.
- Rejected blank direct callers and stored the canonical display name on every
  successful append.
- Added focused XCTest and static contracts for padded unique, duplicate, and
  blank direct-call inputs.
- Updated contributor, security, vision, and changelog guidance.

## Verification Completed

- All four Make gates passed from the checkout and reported that `xcodebuild` was unavailable,
  so this Linux host exercised the complete static baseline.
- The full gate passed from an external directory through the absolute Makefile path.
- `python3 -m py_compile scripts/check-baseline.py`, `sh -n build.sh`, plist,
  storyboard, workspace, project, asset, and workflow parsing, and
  `git diff --check` passed.
- Six isolated hostile mutations were rejected: missing add-boundary
  normalization, raw-name duplicate comparison, raw-name storage, missing
  focused test discovery, stale plan status, and missing verification evidence.
- Exact intended-file generated-artifact and secret-pattern audits passed.
- Hosted macOS app and XCTest-target compilation is recorded separately after
  push; this plan claims only completed local evidence.
