# Changes

## 2026-06-26 12:52 PDT - P2 - Bound normalized travel item names

### Summary
Travel item names are limited to 100 user-perceived characters after normalization.

### Work completed
- Added a model-owned maximum after whitespace canonicalization, shared by UI
  creation, direct collection callers, and initial sample seeding.
- Added exact-limit XCTest coverage for ASCII and emoji grapheme clusters.
- Added static and hostile-mutation contracts plus maintained documentation.

### Validation
- Red phase: the baseline rejected the missing 100-character model boundary.
- `make check` passed the static baseline and build wrapper; `xcodebuild` was
  unavailable locally and skipped explicitly.
- Fifteen hostile mutations, including removal of the model guard, XCTest, or
  documentation contract, were rejected.
- `git diff --check` passed.

### Bugs / findings
- P2: arbitrarily large local item strings could enter memory and table labels.

### Blockers
- Hosted macOS CI remains authoritative for Swift compilation and XCTest.

### Next action
- Open the PR, run Codex review, and merge only after hosted checks pass.

## 2026-06-26 00:13 PDT - P2 - Clarify in-memory data ownership

### Summary
The project now states exactly where travel items live, when they reset, and
which persistence and transmission behaviors do not exist.

### Work completed
- Documented controller-owned process-memory storage and one-shot sample reset
  behavior without adding persistence.
- Made the absence of disk storage, backup, export, sync, analytics, and list
  logging explicit in user and security guidance.
- Closed the stale persistence-clarification roadmap item while preserving a
  design gate for any future storage or transfer feature.
- Added baseline and hostile-mutation contracts for the ownership boundary.

### Threads
- None; work completed directly in this maintenance cycle.

### Files changed
- `README.md`, `SECURITY.md`, and `VISION.md` — lifetime, privacy, and roadmap
  contracts.
- `scripts/check-baseline.py` and `scripts/test-check-baseline.py` — static and
  hostile-mutation coverage.
- `docs/plans/2026-06-26-in-memory-data-ownership.md` and `CHANGES.md` — plan
  and cycle evidence.

### Validation
- Red phase: `python3 scripts/check-baseline.py` rejected all four missing
  ownership and roadmap contracts before documentation was added.
- `make check` passed the static baseline, build wrapper, and ten hostile
  contract mutations.
- `git diff --check` passed.
- `codex review --base origin/master` was attempted but the external service
  returned HTTP 401 before analysis; manual diff review found no actionable
  issue, and the run continued under the instruction to skip authentication
  failures.
- Hosted Xcode and exact merge verification remain required before merge.

### Bugs / findings
- P2: The README said the app was local-first and in-memory, but did not define
  controller lifetime, reset behavior, or the complete absence of durable and
  transmitted data paths.

### Blockers
- `xcodebuild` is unavailable locally; hosted macOS CI is authoritative for the
  app and XCTest build.
- External Codex review authentication is unavailable in this environment.

### Next action
- Open the PR, run Codex review, and merge only after hosted checks pass.

## 2026-06-25 - P2 - Seed defaults through the add boundary

### Summary
Routed initial Phone, Wallet, and Passport rows through the normalized
duplicate-aware collection boundary.

### Work completed
- Preserved one-shot controller ownership and empty-list sample order.
- Added XCTest for an equivalent preexisting default.
- Added two hostile mutations; the rebased combined suite now rejects twelve.

### Validation
- `python3 scripts/check-baseline.py` failed before implementation and passed after.
- `/usr/bin/make check` and the absolute external-directory Make gate passed;
  the rebased combined suite rejected twelve mutations, while `xcodebuild` was
  unavailable locally and skipped explicitly.
- `git diff --check` passed.
- `codex review --base origin/master` was attempted on the rebased exact diff,
  but the external service returned HTTP 401 before analysis; manual review of
  the source, XCTest, contracts, and merged documentation found no actionable
  issue, and the run continued under the instruction to skip auth failures.

### Bugs / findings
- P2: direct initial appends could duplicate an equivalent preexisting default.

### Blockers
- Hosted macOS CI remains authoritative for Swift compiler and XCTest evidence.
- External Codex review authentication is unavailable in this environment.

### Next action
- Merge only after exact-head Codex/manual review and hosted checks pass.

## 2026-06-25 04:54 - P2 - Make sample seeding idempotent

### Summary
Made initial Phone, Wallet, and Passport seeding one-shot per table controller so
repeated view setup cannot duplicate defaults or restore deleted rows.

### Work completed
- Added an explicit initial-data lifecycle flag.
- Added XCTest and static regression contracts for repeated seeding calls.

### Threads
- Started: none — work completed directly in the current repository.
- Continued: none.
- Stopped: none.

### Files changed
- `TravelList/TravelListTableViewController.swift` — guarded initial seeding.
- `TravelListTests/TravelListTests.swift` — added the idempotency regression.
- `scripts/check-baseline.py` — required the one-shot lifecycle contract.
- Documentation and plan files — recorded behavior and validation limits.

### Validation
- `python3 scripts/check-baseline.py` — failed before implementation and passed after.
- `/usr/bin/make check` — passed the baseline, six mutation checks, and the
  conditional build gate; Xcode was unavailable locally.
- `git diff --check` — passed.

### Bugs / findings
- P2: repeated `loadInitialData()` calls appended duplicate sample rows; an
  emptiness-only guard would also restore defaults after users deleted all rows.

### Blockers
- `xcodebuild` is unavailable locally; hosted macOS CI remains authoritative for
  app and XCTest compilation/execution.

### Next action
- Open a PR and complete Codex plus hosted review before merge.

## 2026-06-21

- Aligned target-local app and XCTest bundle identifiers with their existing
  Info.plist identifiers and added a static mismatch regression contract.

## 2026-06-19

- Collapsed accepted horizontal Unicode whitespace to ordinary spaces and used
  a fixed-locale case- and width-insensitive duplicate key for new and existing
  travel item names.
- Added simulator XCTest coverage and five mutation-sensitive baseline checks
  for the corrected canonicalization boundary.

## 2026-06-17

- Rejected embedded Unicode line separators at the shared travel-item name
  boundary and added focused XCTest coverage.

## 2026-06-16

- Rejected embedded control characters at the shared travel-item name boundary
  while preserving ordinary internationalized display names.

## 2026-06-15

- Normalized existing item names during duplicate checks so legacy or direct
  noncanonical rows cannot admit an equivalent canonical item.

## 2026-06-14

- Canonicalized direct travel-item additions before duplicate comparison and
  rejected blank names at the collection mutation boundary.

## 2026-06-13

- Made all Make verification aliases location-independent when invoked through
  an absolute Makefile path.
- Added case-insensitive duplicate item checks before user-added list mutation
  and table reload.

## 2026-06-12

- Added an app-hosted `TravelListTests` target and made `make check` compile the
  unsigned app and XCTest bundle together.

## 2026-06-10

- Migrated the app and checked-in test source to Swift 5 and iOS 12.
- Replaced `NSMutableArray` list storage with typed `[TravelListItem]` storage.
- Added an unsigned simulator app build to `make check` and hosted macOS CI.
- Guarded add-screen textfield outlet reads so missing storyboard wiring falls
  back through the shared name normalizer.
- Added pinned, read-only macOS GitHub Actions project validation for
  `make check` and `TravelList.xcodeproj` parsing without persisted checkout
  credentials.

## 2026-06-09

- Added local `make lint`, `make test`, and `make build` gate aliases for the
  static Travel List baseline.
- Added a removal index guard so invalid travel item selections do not mutate
  the local list.
- Scoped the travel logo to each navigation item title view instead of adding
  navigation-controller overlay subviews.

## 2026-06-08

- Trimmed new travel item names before accepting them so whitespace-only entries are ignored.
- Moved travel item trimming into a shared name normalizer on the model.
- Replaced generated test placeholders with normalizer tests for trimmed, blank, and missing item names.
- Avoided force-unwrapping travel item text and reset pending items before each add segue.
- Guarded storyboard/table cell casts and invalid delete indexes.
- Guarded table cell indexes before reading list data during rendering.
- Switched cell rendering to a configurable fallback cell when storyboard reuse wiring is unavailable.
- Cleared stale cell text and accessory state before returning fallback cells for invalid or malformed rows.
- Rejected partial invalid hex color scans so malformed colors fall back to gray.
- Removed table reload work from cell rendering.
- Added `make check` and a static Swift/Xcode baseline for plist/storyboard/asset metadata, source inventory, list-flow guardrails, and local-first privacy checks.
- Documented the legacy Xcode project, local-first list behavior, and static verification workflow.
