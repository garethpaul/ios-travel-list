# Cell Index Guard Plan

status: completed

## Context

`ios-travel-list` already guards invalid delete indexes and storyboard casts. `cellForRowAtIndexPath` still reads `travelItems` before validating the row, which can crash if local table state becomes stale.

## Objectives

- Guard cell-render indexes before reading from `travelItems`.
- Return the dequeued fallback cell when the row is invalid.
- Keep cell rendering side-effect free.
- Extend the static baseline so cell rendering keeps both index and reload guards.

## Verification

- `make check`
- `python3 scripts/check-baseline.py`
- `git diff --check`
