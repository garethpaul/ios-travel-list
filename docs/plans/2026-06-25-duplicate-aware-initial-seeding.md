---
status: completed
date: 2026-06-25
---

# Duplicate-Aware Initial Seeding

## Context

One-shot lifecycle ownership prevents repeated setup from appending the sample
rows twice, but `loadInitialData()` still wrote directly to `travelItems`.
That bypassed the normalized duplicate-aware insertion boundary used for user
items and could add a second Phone, Wallet, or Passport when a controller was
prepopulated before initial setup.

## Decision

Seed the three defaults through `addTravelItem(_:)` after claiming the existing
one-shot flag. Preserve the current sample order for an empty controller and
silently retain an equivalent preexisting item instead of appending a duplicate.

## Work Completed

- Routed Phone, Wallet, and Passport through the canonical collection boundary.
- Added XCTest for a preexisting case-insensitive Phone item.
- Strengthened the portable lifecycle contract and added two hostile mutations
  for source bypass and missing XCTest evidence.
- Updated maintenance, privacy, and project-direction documentation.

## Verification Completed

- `python3 scripts/check-baseline.py` failed before implementation on the direct
  sample append path and passed afterward.
- `/usr/bin/make check` passed the static baseline and eight hostile mutations;
  `xcodebuild` was unavailable locally and skipped explicitly.
- All four Make gates passed from the checkout and through the absolute
  Makefile path from `/tmp`.
- `python3 -m py_compile scripts/check-baseline.py scripts/test-check-baseline.py`
  and `git diff --check` passed.

## Scope Boundaries

- Item names, sample order on an empty controller, one-shot lifecycle behavior,
  add/remove UI, completion state, memory-only storage, and privacy behavior are
  otherwise unchanged.
- Local UIKit/XCTest execution is not claimed without Xcode; hosted macOS CI is
  authoritative for compiler and XCTest evidence.
