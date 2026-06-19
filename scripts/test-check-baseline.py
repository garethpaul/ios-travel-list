#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


MUTATIONS = [
    (
        "remove width-insensitive duplicate folding",
        "TravelList/TravelListItem.swift",
        ".caseInsensitive, .widthInsensitive",
        ".caseInsensitive",
    ),
    (
        "replace fixed duplicate locale",
        "TravelList/TravelListItem.swift",
        'Locale(identifier: "en_US_POSIX")',
        "Locale.current",
    ),
    (
        "remove horizontal whitespace canonicalization",
        "TravelList/TravelListItem.swift",
        "components(separatedBy: .whitespaces)",
        "components(separatedBy: .newlines)",
    ),
    (
        "bypass model-owned existing duplicate key",
        "TravelList/TravelListTableViewController.swift",
        "TravelListItem.duplicateKey(forNormalizedName: existingName) == duplicateKey",
        "existingName == normalizedName",
    ),
    (
        "remove width-variant XCTest evidence",
        "TravelListTests/TravelListTests.swift",
        "testAddTravelItemRejectsWidthVariantDuplicate",
        "testAddTravelItemAllowsWidthVariantDuplicate",
    ),
]


def main():
    baseline_result = subprocess.run(
        [sys.executable, "scripts/check-baseline.py"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if baseline_result.returncode != 0:
        print("unmutated baseline must pass before mutation testing", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="ios-travel-list-mutations-") as temporary_directory:
        temporary_root = Path(temporary_directory) / "checkout"
        shutil.copytree(
            ROOT,
            temporary_root,
            ignore=shutil.ignore_patterns(".git", "build", "DerivedData", "*.xcresult"),
        )

        for description, relative_path, original, replacement in MUTATIONS:
            mutation_root = Path(temporary_directory) / description.replace(" ", "-")
            shutil.copytree(temporary_root, mutation_root)
            mutation_path = mutation_root / relative_path
            contents = mutation_path.read_text(encoding="utf-8")
            if contents.count(original) != 1:
                print(f"mutation fixture mismatch for {description}", file=sys.stderr)
                return 1
            mutation_path.write_text(contents.replace(original, replacement, 1), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "scripts/check-baseline.py"],
                cwd=mutation_root,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if result.returncode == 0:
                print(f"baseline accepted hostile mutation: {description}", file=sys.stderr)
                return 1

    print(f"Rejected {len(MUTATIONS)} Unicode canonicalization mutations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
