# Canonical Travel Item Add Boundary

status: planned

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
