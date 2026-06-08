## iOS Travel List Vision

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
- Maintain a small Xcode project structure

Next priorities:

- Add README setup and verification instructions
- Strengthen tests around adding, displaying, and clearing travel items
- Modernize Swift/project settings in a dedicated pass
- Clarify persistence behavior and data ownership

Contribution rules:

- One PR = one focused list, UI, storage, test, or documentation change.
- Verify app flow after storyboard or controller changes.
- Keep generated build products and signing files out of git.
- Document any change that stores or transmits list data.

## Security And Privacy

Canonical security policy and reporting:

- [`SECURITY.md`](SECURITY.md)

Travel lists can reveal personal plans. The app should remain local by default
and avoid logging, syncing, or uploading item data without clear user action.

## What We Will Not Merge (For Now)

- Background sync or upload without privacy design
- List-content logging
- Broad project migration mixed with storage behavior changes
- Generated signing material

This list is a roadmap guardrail, not a permanent rule.
Strong user demand and strong technical rationale can change it.
