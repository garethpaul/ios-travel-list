# AGENTS.md

## Repository purpose

`garethpaul/ios-travel-list` is an Apple platform application or Swift sample. Travel List so you don't forget things.

## Project structure

- `Makefile` - repository verification targets
- `scripts` - baseline checks and helper scripts
- `docs` - plans, notes, and generated README assets
- `TravelList.xcodeproj` - Xcode project
- `img` - repository source or sample assets
- `TravelList` - repository source or sample assets
- `TravelListTests` - repository source or sample assets

## Development commands

- Install dependencies: no repository-specific install command is documented.
- Full baseline: `make check`
- Local Apple development: `open TravelList.xcodeproj`
- If a command above skips because a platform toolchain is missing, verify on a machine with that SDK before claiming platform behavior is tested.

## Coding conventions

- Language mix noted in the README: Swift 5, Python 3, and a legacy C header.
- Preserve the iOS 12 deployment target and unsigned simulator build assumptions unless the change is explicitly about modernization.

## Testing guidance

- Test-related files detected: `docs/plans/2026-06-09-travel-item-normalizer-tests.md`, `TravelListTests/TravelListTests.swift`
- Start with the narrowest relevant test or Make target, then run `make check` before handing off if the change is not documentation-only.
- Keep README verification notes in sync when commands, fixtures, or supported toolchains change.

## PR / change guidance

- Keep diffs focused on the requested repository and avoid unrelated modernization or formatting churn.
- Preserve public APIs, sample behavior, file formats, and documented environment variables unless the task explicitly changes them.
- Update tests, README notes, or docs/plans when behavior, security posture, or validation commands change.
- Call out skipped platform validation, legacy toolchain assumptions, and any risky files touched in the final summary.

## Safety and gotchas

- No required secret or credential file was identified in the repository scan. If you add integrations later, keep secrets out of git.
- Travel lists can reveal personal plans. Keep list data local-first unless a future change documents storage, sync, consent, and deletion behavior.
- Cell rendering should remain side-effect free and validate row indexes before reading list data; avoid reloading the table from inside `cellForRowAtIndexPath`.
- Keep fallback cell handling configurable so valid rows can still display item text if storyboard reuse wiring changes.
- Clear stale cell text and accessory state before returning fallback cells for invalid or malformed rows.
- Keep `TravelListTests.swift` attached to the app-hosted XCTest target and compiler-checked by `make check`.
- Keep storyboard casts, text-field reads, table indexes, and color parsing guarded so malformed local UI state falls back safely.

## Agent workflow

1. Inspect the README, Makefile, manifests, and the files directly related to the request.
2. Make the smallest source or docs change that satisfies the task; avoid generated, vendored, or local-environment files unless required.
3. Run the narrowest useful validation first, then `make check` or the documented package/platform gate when available.
4. If a required SDK, service credential, or external runtime is unavailable, record the skipped command and why.
5. Summarize changed files, commands run, and remaining risks or follow-up validation.
