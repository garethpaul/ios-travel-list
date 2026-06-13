# Duplicate Travel Item Guard

status: completed

## Context

The add flow normalizes blank and whitespace-only names, then appends every
valid `TravelListItem`. Users can therefore add duplicate checklist rows,
including case variants of the seeded Phone, Wallet, and Passport items.

## Priority

A checklist should keep one row per normalized item name. Duplicate entries
make removal ambiguous and can produce accidental repeated packing tasks from a
single Done action sequence.

## Requirements

- R1. Add one testable list helper that returns whether an item was appended.
- R2. Reject an item when an existing normalized item name compares equal
  case-insensitively.
- R3. Reload the table only after a successful append.
- R4. Preserve input normalization, cancel fail-closed behavior, seeded items,
  removal semantics, cell fallback behavior, layout, and local-only storage.
- R5. Add focused XCTest assertions, static contracts, documentation, and
  completed verification evidence.

## Implementation Units

### U1. Centralize guarded append behavior

- **File:** `TravelList/TravelListTableViewController.swift`
- Add a Boolean append helper and route the unwind action through it.

### U2. Cover duplicate semantics

- **File:** `TravelListTests/TravelListTests.swift`
- Assert successful unique append and rejection of same-case and case-variant
  duplicates without changing list count.

### U3. Enforce and document the contract

- **Files:** `scripts/check-baseline.py`, `README.md`, `SECURITY.md`,
  `VISION.md`, `CHANGES.md`
- Require case-insensitive duplicate detection, Boolean result use, reload
  ordering, tests, and completed plan evidence.

## Scope Boundaries

- Do not change initial item names, text normalization, deletion-on-selection,
  storyboard wiring, persistence, networking, analytics, upload, or logging.
- Do not introduce locale-dependent canonicalization beyond the existing
  normalized display names and case-insensitive comparison.
- Do not claim interactive simulator validation without Xcode.

## Work Completed

- Added a Boolean append helper that rejects case-insensitive name matches
  before mutating the typed local list.
- Routed the unwind action through the helper and reloads only after success.
- Added focused XCTest assertions and static/documentation contracts.

## Verification Completed

- All four Make gates, `make lint`, `make test`, `make build`, and `make check`,
  passed against the complete static baseline.
- `python3 -m py_compile scripts/check-baseline.py`, plist parsing, storyboard,
  workspace, and SVG XML parsing, asset/workflow JSON and YAML parsing, PNG
  validation, `sh -n build.sh`, and `git diff --check` passed.
- Seven hostile mutations removing duplicate detection, weakening comparison,
  appending before the guard, reloading on rejection, or removing focused tests
  or falsifying plan status or verification evidence were rejected.
- The local environment did not provide `xcodebuild`, so XCTest execution and
  interactive storyboard validation were not claimed.
