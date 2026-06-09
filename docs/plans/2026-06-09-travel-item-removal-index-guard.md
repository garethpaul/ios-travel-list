# Travel Item Removal Index Guard

status: completed

## Context

The table selection path removed travel items directly from the backing array.
It already ignored out-of-range table rows, but the removal rule was embedded in
the UI delegate and had no focused XCTest coverage.

## Objectives

- Move travel item deletion into a small guarded helper.
- Reject negative and out-of-range removal indexes before mutating the list.
- Reload the table only after a valid removal succeeds.
- Add focused XCTest coverage for valid and invalid removal indexes.
- Extend the static baseline and docs so the removal guardrail remains visible.

## Verification

- `make check`
- `python3 scripts/check-baseline.py`
- `git diff --check`
