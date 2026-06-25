# Idempotent Initial Items

## Status: Completed

## Context

`loadInitialData()` appended Phone, Wallet, and Passport every time it ran.
Repeated view setup or direct lifecycle calls could therefore duplicate sample
rows. Guarding only on an empty array would reintroduce deleted defaults after a
user removed every item.

## Design

Track whether the controller has attempted initial seeding with a private
boolean. The first call marks the lifecycle step complete and appends the same
three sample rows; later calls are no-ops regardless of current list contents.

Calling `addTravelItem()` for each seed was rejected because it changes the
existing direct sample setup and still does not model one-shot lifecycle intent.

## Work Completed

- Added a private one-shot initial-data flag.
- Added XCTest coverage that calls the method twice and expects exactly the
  original ordered sample rows.
- Added a mutation-sensitive static source contract and maintenance docs.

## Verification

- `python3 scripts/check-baseline.py`
- `/usr/bin/make check`
- `git diff --check`
- Local `xcodebuild` was unavailable; hosted macOS CI supplies project build and
  XCTest evidence.

## Scope Boundaries

- Item normalization, duplicate detection, deletion, completion state, cell
  rendering, storyboard wiring, persistence, and sync behavior are unchanged.
- No device data, network access, or hidden storage was introduced.
