## iOS Travel List Vision

This document explains the current state and direction of the project.
Project overview and developer docs: [`README.md`](README.md)

iOS Travel List is a simple Swift travel companion app for tracking items so
they are not forgotten while traveling.

The repository is useful as a small list-management iOS sample with item entry,
table display, tests, and a screenshot. Project context lives in
[`README.md`](README.md).

The goal is to keep the app local-first, simple, and easy to build.

The current focus is:

Priority:

- Preserve add-item and list-display behavior
- Keep screenshot and README aligned with app behavior
- Avoid syncing or uploading travel-list data without explicit design
- Keep normalizer tests focused on trimmed, blank, missing, embedded-control,
  Unicode line separators, and internationalized travel item names
- Keep add-screen textfield outlet reads guarded before item creation
- Keep table rendering guarded against stale local indexes
- Keep item removal index handling guarded before local list mutation
- Keep duplicate item checks case-insensitive and ahead of list mutation
- Keep collection add-boundary normalization ahead of duplicate checks and store
  only canonical display names
- Keep initial sample data one-shot per controller so lifecycle callbacks do not
  duplicate or restore list rows
- Keep process-memory-only item ownership and reset behavior explicit until a
  separate persistence design is approved
- Keep initial defaults on the canonical duplicate-aware collection boundary
- Keep fallback cell rendering configurable for valid rows
- Clear stale cell state when invalid or malformed rows use fallback cells
- Keep the travel logo scoped to each navigation item title view
- Keep travel-item storage strongly typed in Swift
- Maintain a small Xcode project structure
- Keep `make lint`, `make test`, `make build`, and `make check` available as
  local verification gates
- Keep GitHub Actions project validation pinned and read-only on macOS through an
  unsigned app build in `make check`
- Keep checkout credential-free so build steps cannot reuse the workflow token
- Keep `scripts/check-baseline.py` passing for local-first list behavior,
  item trimming, storyboard wiring, Xcode metadata, and source inventory

Next priorities:

- Strengthen tests around adding, displaying, and clearing travel items
- Add an XCTest target for the checked-in normalization and removal tests

Contribution rules:

- One PR = one focused list, UI, storage, test, or documentation change.
- Verify app flow after storyboard or controller changes.
- Run `make lint`, `make test`, `make build`, and `make check` before pushing
  source, project metadata, asset, list-flow, or privacy changes.
- Keep generated build products and signing files out of git.
- Document any change that stores or transmits list data.

## Security And Privacy

Canonical security policy and reporting:

- [`SECURITY.md`](SECURITY.md)

Travel lists can reveal personal plans. The app should remain local by default
and avoid logging, syncing, or uploading item data without clear user action.

Current baseline: `make lint`, `make test`, `make build`, and `make check` run
`scripts/check-baseline.py` and compile the app and XCTest target when Xcode is available. They verify plist/storyboard/asset
metadata, local-first list flow, whitespace trimming through a shared name normalizer,
normalizer tests, guarded textfield outlet reads, guarded storyboard/table flows,
cell index checks, removal index checks, side-effect-free cell rendering,
fallback cell handling, stale cell reset handling, navigation logo title view
ownership, invalid color fallback, and no logging, network, upload, analytics,
or persistence behavior.

## What We Will Not Merge (For Now)

- Background sync or upload without privacy design
- List-content logging
- Broad project migration mixed with storage behavior changes
- Generated signing material

This list is a roadmap guardrail, not a permanent rule.
Strong user demand and strong technical rationale can change it.
