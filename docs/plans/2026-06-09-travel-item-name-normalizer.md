# Travel Item Name Normalizer

status: completed

## Context

The add screen trimmed travel item text inline before creating a
`TravelListItem`. Keeping that rule in the model gives the list flow one shared
place for blank-name rejection and makes future entry points less likely to
accept whitespace-only items.

## Objectives

- Add a shared optional name normalizer to `TravelListItem`.
- Use the shared normalizer from `AddTravelViewController`.
- Preserve rejection of blank or whitespace-only item names.
- Extend the static baseline and docs to capture the name normalizer guard.

## Verification

- `make check`
- `git diff --check`
