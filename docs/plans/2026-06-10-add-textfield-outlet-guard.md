# Add Textfield Outlet Guard

status: completed

## Context

`AddTravelViewController` already clears stale pending items and sends text
through `TravelListItem.normalizedName`, but the text read still went through an
implicitly unwrapped storyboard outlet. If the add screen outlet is missing or
not connected during a future storyboard edit, the existing nil-normalizer path
should handle that state instead of crashing.

## Completed Scope

- Changed add-screen text reads to use optional chaining on the text field
  outlet.
- Kept blank and missing item names rejected by the shared normalizer.
- Extended the static baseline and docs so textfield outlet reads stay guarded
  without adding persistence, sync, upload, analytics, or network behavior.

## Verification

- `make check`
- `python3 scripts/check-baseline.py`
- `git diff --check`
