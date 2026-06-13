# Duplicate Travel Item Guard

status: planned

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

## Verification

- `make lint`
- `make test`
- `make build`
- `make check`
- `python3 -m py_compile scripts/check-baseline.py`
- Parse plist, storyboard, workspace, project, workflow, JSON, SVG, and PNG
  metadata with available local parsers.
- `sh -n build.sh`
- `git diff --check`
- Hostile mutations removing duplicate detection, weakening case-insensitive
  comparison, appending before the guard, reloading on rejection, removing
  focused tests, or falsifying plan evidence must be rejected.
