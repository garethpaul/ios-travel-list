# iOS Travel List Baseline Plan

status: completed

## Context

`ios-travel-list` is a legacy Swift iOS list-management sample with storyboard UI, local in-memory items, image assets, and a small test target. This Linux host does not provide Xcode, so local verification needs a static baseline while full app builds remain a macOS/Xcode responsibility.

## Objectives

- Trim new item names and reject whitespace-only entries.
- Avoid force-unwrapping text fields, storyboard cells, and invalid table indexes.
- Reject partial invalid hex color scans.
- Keep cell rendering side-effect free by avoiding table reloads from `cellForRowAtIndexPath`.
- Add a local `make check` baseline for Xcode metadata, plist/storyboard/asset JSON, source inventory, list-flow guardrails, and local-first privacy checks.
- Document legacy Xcode verification expectations and non-macOS static checks.

## Verification

- `make check`
- `python3 scripts/check-baseline.py`
- `git diff --check`
