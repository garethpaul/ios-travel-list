# Travel Item Length Boundary

Status: Completed

## Goal

Prevent arbitrarily large travel item strings from entering controller memory
or table rendering while preserving internationalized names.

## Scope

- Measure the canonical stored name after whitespace normalization.
- Accept at most 100 Swift `Character` values.
- Reject longer names through the shared model boundary.
- Cover ASCII and emoji exact-limit behavior in XCTest.

## Verification

- Prove the missing model guard through the static baseline.
- Run `make check` and hostile mutations.
- Run hosted Xcode build and XCTest before merge.
- Run `git diff --check` and exact-head review.

## Outcome

Every add path now shares a 100-user-perceived-character bound after
normalization without byte or UTF-16 truncation.
