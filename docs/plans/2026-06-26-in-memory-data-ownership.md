# In-Memory Data Ownership Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use executing-plans to implement this plan task-by-task.

## Status: Completed

**Goal:** Explain exactly where travel items live, when they reset, and what the app does not persist or transmit.

**Architecture:** Preserve the existing typed controller-owned array and one-shot sample seeding. Add a README privacy/status section, align the roadmap and security policy, and enforce the claims through the existing dependency-free baseline.

**Tech Stack:** Swift UIKit source inspection, Markdown, Python 3 static contracts, GNU Make.

---

### Task 1: Add the failing ownership contract

**Files:**
- Modify: `scripts/check-baseline.py`
- Modify: `scripts/test-check-baseline.py`

**Step 1:** Require documentation stating that items remain only in the current controller's in-memory array, are not written to disk or transmitted, and reset to the sample list after a new controller/app process.

**Step 2:** Run `python3 scripts/check-baseline.py` and confirm failure before documentation exists.

### Task 2: Document current behavior

**Files:**
- Modify: `README.md`
- Modify: `SECURITY.md`
- Modify: `VISION.md`
- Modify: `CHANGES.md`
- Modify: `docs/plans/2026-06-26-in-memory-data-ownership.md`

**Step 1:** Add the exact in-memory lifetime and ownership boundary.

**Step 2:** Remove the completed persistence-clarification roadmap item without adding persistence, sync, export, analytics, or logging.

**Step 3:** Mark this plan completed and record validation evidence.

### Task 3: Validate

**Files:**
- Test: `scripts/check-baseline.py`
- Test: `scripts/test-check-baseline.py`

**Step 1:** Run `make check`.

**Step 2:** Remove each required documentation claim in isolated copies and confirm the baseline rejects it.

**Step 3:** Run `git diff --check` and commit with `docs: clarify in-memory data ownership`.

## Completed Work

- Added a README ownership and lifetime section grounded in the typed
  controller-owned array and one-shot sample seeding.
- Documented that the app has no disk persistence, backup, export, sync,
  analytics, upload, or list logging behavior.
- Added the future consent, retention, deletion, transfer, and ownership design
  boundary to security and roadmap documentation.
- Added static and hostile-mutation contracts for the completed clarification.

## Verification

- `python3 scripts/check-baseline.py`
- `python3 scripts/test-check-baseline.py`
- `make check`
- `git diff --check`

## Scope Boundaries

- No Swift source, storyboard, Xcode project, app behavior, persistence, sync,
  logging, analytics, export, or network behavior changed.
- No simulator, device, user data, or storage service was exercised locally.
