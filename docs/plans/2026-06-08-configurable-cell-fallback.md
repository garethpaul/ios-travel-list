# Configurable Cell Fallback Plan

status: completed

## Context

`TravelListTableViewController` guards missing storyboard cell reuse wiring by returning an empty `UITableViewCell`. That avoids a crash, but valid rows cannot display item text when the storyboard dequeue fails.

## Objectives

- Use a default reusable cell fallback when storyboard dequeue returns nil.
- Keep valid row rendering configurable through the same cell setup path.
- Preserve index guards before reading from `travelItems`.
- Extend the static baseline so the configurable fallback remains visible.

## Verification

- `make check`
- `python3 scripts/check-baseline.py`
- `git diff --check`
