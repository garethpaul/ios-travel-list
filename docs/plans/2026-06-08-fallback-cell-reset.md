# Fallback Cell Reset Plan

status: completed

## Context

The list controller uses a configurable fallback table cell when storyboard reuse
wiring is unavailable. Invalid indexes or malformed row data should not return a
reused cell with stale item text from an earlier row.

## Objectives

- Centralize table-cell configuration in a helper.
- Clear fallback cell text and accessory state before returning invalid or
  malformed rows.
- Preserve valid-row display and the existing configurable fallback cell.
- Extend the static baseline so stale cell text cannot return through fallback
  paths.
- Document the stale cell reset alongside the existing cell rendering and index
  guardrails.

## Verification

- `make check`
- `python3 scripts/check-baseline.py`
- `git diff --check`
