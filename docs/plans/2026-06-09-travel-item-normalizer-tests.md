# Travel Item Normalizer Tests

status: completed

## Context

`TravelListItem.normalizedName` now owns trimming and blank-name rejection, but
the checked-in XCTest file still contained generated placeholder tests. The
normalizer should have focused assertions so future changes do not weaken item
entry behavior silently.

## Objectives

- Replace generated XCTest placeholders with travel item normalizer assertions.
- Cover trimmed, blank, and missing item names.
- Keep the app target testable from XCTest in Debug builds.
- Extend the static baseline so placeholder tests do not return.
- Preserve local-first behavior without adding persistence, sync, uploads,
  analytics, or logging.

## Verification

- `make check`
- `python3 scripts/check-baseline.py`
- `git diff --check`
