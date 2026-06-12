# iOS Travel List CI Baseline

status: completed

## Context

The sample began with an SDK-free `make check` baseline for list behavior,
metadata, image assets, docs, and local-first privacy guardrails. Hosted CI now
runs that baseline on macOS and compiles the unsigned app when Xcode is present.

## Changes

- Added `.github/workflows/check.yml` for GitHub Actions, then advanced it to a
  pinned, read-only, bounded `macos-15` job.
- Disabled persisted checkout credentials.
- Run the Python static baseline and unsigned simulator build through the same
  `make check` entry point.
- Keep simulator interaction, signed installation, and device verification as
  separate macOS developer tasks.
- Extended the checker and docs so hosted CI stays visible.

## Verification

- `make check`
- `git diff --check`
