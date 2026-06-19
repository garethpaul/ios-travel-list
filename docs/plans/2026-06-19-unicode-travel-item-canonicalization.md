# Unicode Travel Item Canonicalization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use executing-plans to implement this plan task-by-task.

**Goal:** Make travel checklist names use one stable display normalization and one locale-independent duplicate key across typed and existing list items.

**Architecture:** Keep validation and canonicalization owned by `TravelListItem`, then have `TravelListTableViewController` compare only model-provided duplicate keys before mutating the list. Preserve local-only storage and the existing Boolean add boundary; do not add persistence or broaden the UI architecture.

**Tech Stack:** Swift 5, Foundation Unicode APIs, UIKit, XCTest, Python baseline contracts, Xcode simulator builds.

---

### Task 1: Prove Unicode Canonicalization Defects

**Files:**
- Test: `TravelListTests/TravelListTests.swift`

**Step 1: Write failing normalization tests**

Add an XCTest case showing that Unicode horizontal whitespace runs normalize to one ASCII space. Confirm separately that the existing control-character guard already rejects invisible formatting controls.

**Step 2: Write failing duplicate tests**

Add XCTest cases showing that full-width compatibility forms and non-breaking-space variants cannot bypass duplicate detection against existing items.

**Step 3: Run tests to verify failure**

Run:

```sh
xcodebuild -project TravelList.xcodeproj -scheme TravelList -sdk iphonesimulator -destination 'platform=iOS Simulator,name=iPhone 16e' test
```

Expected: the new Unicode normalization and duplicate assertions fail against PR #9.

### Task 2: Centralize Stable Model Canonicalization

**Files:**
- Modify: `TravelList/TravelListItem.swift`
- Modify: `TravelList/TravelListTableViewController.swift`
- Test: `TravelListTests/TravelListTests.swift`

**Step 1: Implement minimal display normalization**

Preserve the existing control/newline rejection and collapse accepted horizontal Unicode whitespace runs to one ASCII space.

**Step 2: Implement a locale-independent duplicate key**

Fold case and width using a fixed POSIX locale, then precompose the result for stable Unicode comparison.

**Step 3: Use the duplicate key at the collection boundary**

Compare model-provided keys for both the incoming name and every existing item before appending or reloading the table.

**Step 4: Run focused XCTest**

Run the simulator test command and expect all XCTest cases to pass.

### Task 3: Strengthen Static and Mutation Evidence

**Files:**
- Modify: `scripts/check-baseline.py`
- Modify: `CHANGES.md`
- Modify: `README.md`

**Step 1: Add source contracts**

Require the existing control rejection, horizontal whitespace collapse, fixed-locale width/case duplicate key, and controller use of that key.

**Step 2: Add mutation-sensitive checks**

Run isolated source mutations that remove each invariant and verify `scripts/check-baseline.py` rejects every mutated checkout.

**Step 3: Document behavior and evidence**

Record the corrected duplicate and display normalization behavior without claiming persistence, device, or legacy iOS runtime coverage.

### Task 4: Validate and Land the Stack

**Files:**
- Verify: entire checkout

**Step 1: Run local gates**

Run `make lint`, `make test`, `make build`, `make check`, the simulator XCTest command, external-directory Make verification, syntax checks, mutation checks, and `git diff --check`.

**Step 2: Commit and push the reviewed head**

Create one focused review-fix commit on top of PR #9 and push it to an aggregate review branch.

**Step 3: Require hosted proof**

Open an aggregate PR, wait for exact-head Check and CodeQL success, and respect branch protection or review gates.

**Step 4: Merge and reconcile original PRs**

Merge only when supported, verify the exact tree on `master`, then mark #3-#9 merged or close only genuinely superseded refs with evidence.

## Verification Completed

- RED: Xcode simulator XCTest failed with five assertions because PR #9
  accepted full-width and Unicode-horizontal-whitespace duplicate variants and
  preserved noncanonical internal spacing.
- GREEN: Xcode 26.0.1 on the iPhone 16e iOS 26 simulator executed 14 XCTest
  cases with zero failures.
- `make lint`, `make test`, `make build`, and `make check` passed from the
  checkout.
- `make -f <absolute checkout>/Makefile check` passed from `/tmp`.
- `python3 -m py_compile scripts/check-baseline.py scripts/test-check-baseline.py`,
  `sh -n build.sh`, and `git diff --check` passed.
- Five isolated hostile source/test mutations were rejected after the
  unmodified baseline passed.
- No persistence implementation exists in this sample; existing in-memory
  items exercise the same collection duplicate boundary, but migration from a
  historical persisted store is not applicable.
- iOS 12 simulator/device behavior, interactive storyboard flows, and physical
  device rendering were unavailable; the current SDK compiled the iOS 12
  deployment target and the current simulator executed the unit tests.
