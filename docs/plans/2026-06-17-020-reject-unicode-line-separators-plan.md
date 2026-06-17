---
title: Unicode Line Separator Guard
type: fix
date: 2026-06-17
---

# Unicode Line Separator Guard

## Summary

Reject every Foundation newline character inside a travel-item name, including
Unicode line and paragraph separators that are not part of the existing control
character set. Preserve trimming and internationalized single-line names.

## Problem Frame

`TravelListItem.normalizedName` trims `whitespacesAndNewlines` at the boundaries
and rejects embedded `controlCharacters`. Apple documents `controlCharacters`
as Unicode categories `Cc` and `Cf`, while `CharacterSet.newlines` separately
includes `U+2028` LINE SEPARATOR and `U+2029` PARAGRAPH SEPARATOR. An embedded
separator therefore survives trimming and can create a visually multi-line item
inside a table row.

Primary references:

- <https://developer.apple.com/documentation/foundation/characterset/controlcharacters>
- <https://developer.apple.com/documentation/foundation/characterset/newlines>

## Requirements

- R1. Reject any normalized item name containing a character from
  `CharacterSet.newlines`.
- R2. Add executable XCTest cases for embedded `U+2028` and `U+2029` values.
- R3. Preserve boundary trimming, blank rejection, control-character rejection,
  internationalized names, canonical direct-add handling, and duplicate rules.
- R4. Extend the canonical checker so it rejects removal of the newline-set
  guard or either Unicode test case.
- R5. Synchronize README, security, vision, and change documentation with the
  single-line item-name boundary.
- R6. Validate locally and from an external directory, reject isolated source,
  test, docs, and checker mutations, and require both hosted workflow events on
  the exact head.

## Key Technical Decisions

- **Use Foundation's standard set:** `CharacterSet.newlines` names the complete
  newline boundary directly and avoids a hand-maintained scalar list.
- **Keep normalization centralized:** both the add form and direct table API
  already call `normalizedName`, so one guard protects every supported entry
  path.
- **Test the uncovered scalars:** existing tests already cover line feed, tab,
  and NUL; the new tests target the two separator categories that motivated the
  fix.

## Implementation Units

### U1. Reject embedded newline separators

- **Goal:** Keep accepted travel-item names single-line across Unicode newline
  representations.
- **Files:** `TravelList/TravelListItem.swift`
- **Verification:** Existing and new normalization tests.
- **Covers:** R1, R3.

### U2. Execute regression coverage

- **Goal:** Prove both Unicode separators fail normalization.
- **Files:** `TravelListTests/TravelListTests.swift`
- **Verification:** Hosted XCTest plus static source/test contracts.
- **Covers:** R2, R3, R4.

### U3. Lock checker and guidance

- **Goal:** Prevent source, test, plan, or documentation drift.
- **Files:** `scripts/check-baseline.py`, `README.md`, `SECURITY.md`, `VISION.md`,
  `CHANGES.md`
- **Verification:** Root/external Make gates and isolated mutations.
- **Covers:** R4, R5, R6.

## Risks And Mitigations

- Broad whitespace rejection could break valid internationalized names; reject
  only Foundation's newline set after the existing boundary trim.
- A source-only guard could regress unnoticed on Linux; require literal XCTest
  cases and retain the hosted macOS test execution boundary.
- Static matching can become ordering-insensitive; assert the newline guard in
  the normalizer and both exact Unicode test expressions.

## Scope Boundaries

- Do not add length limits, persistence, editing, reordering, completion-state
  changes, locale-specific folding, or Unicode compatibility normalization.
- Do not change table rendering, cell reuse, removal behavior, initial data,
  project settings, assets, storyboards, or workflow permissions.
- Do not reject ordinary internal spaces, punctuation, symbols, or accented
  letters.

## Verification

- Run the focused XCTest source contract through `scripts/check-baseline.py`.
- Run `make lint`, `make test`, `make build`, and `make check` from the checkout.
- Run all four Make gates through the absolute Makefile path from an external
  directory.
- Compile the Python checker, validate `build.sh`, and run `git diff --check`.
- Reject isolated mutations for the newline guard, each Unicode scalar test,
  documentation, plan metadata, and checker enforcement.
- Audit the exact diff, generated artifacts, and secret-like values.
- Require exact-head push and pull-request hosted checks before merge.

## Acceptance Criteria

- Embedded `U+2028` and `U+2029` travel-item names normalize to `nil`.
- Existing valid internationalized and boundary-trimmed names remain accepted.
- Both supported add paths retain the centralized normalizer.
- All available local gates and mutations pass, and hosted evidence is recorded
  truthfully for the exact head.
