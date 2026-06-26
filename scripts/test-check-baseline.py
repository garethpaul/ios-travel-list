#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


MUTATIONS = [
    (
        "remove in-memory ownership heading",
        "README.md",
        "## Data Ownership and Lifetime",
        "## Data Lifetime",
    ),
    (
        "claim durable storage",
        "README.md",
        "not written to disk, synced, uploaded, logged, or sent to analytics",
        "written to disk",
    ),
    (
        "remove reset behavior",
        "README.md",
        "A new controller or app process starts again with the checked-in sample items.",
        "The list may remain available indefinitely.",
    ),
    (
        "restore persistence roadmap item",
        "VISION.md",
        "Next priorities:",
        "Next priorities:\n\n- Clarify persistence behavior and data ownership",
    ),
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
    (
        "mismatch release XCTest bundle identifier",
        "TravelList.xcodeproj/project.pbxproj",
        "\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.garethpaul.TravelListTests;\n"
        '\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";\n'
        "\t\t\t\tSWIFT_VERSION = 5.0;\n"
        "\t\t\t\tTARGETED_DEVICE_FAMILY = 1;\n"
        '\t\t\t\tTEST_HOST = "$(BUILT_PRODUCTS_DIR)/TravelList.app/TravelList";\n'
        "\t\t\t};\n"
        "\t\t\tname = Release;",
        "\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.garethpaul.WrongTests;\n"
        '\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";\n'
        "\t\t\t\tSWIFT_VERSION = 5.0;\n"
        "\t\t\t\tTARGETED_DEVICE_FAMILY = 1;\n"
        '\t\t\t\tTEST_HOST = "$(BUILT_PRODUCTS_DIR)/TravelList.app/TravelList";\n'
        "\t\t\t};\n"
        "\t\t\tname = Release;",
    ),
    (
        "bypass duplicate-aware initial seeding",
        "TravelList/TravelListTableViewController.swift",
        "_ = addTravelItem(TravelListItem(name: itemName))",
        "travelItems.append(TravelListItem(name: itemName))",
    ),
    (
        "remove preexisting default seed XCTest evidence",
        "TravelListTests/TravelListTests.swift",
        "testLoadInitialDataDoesNotDuplicateExistingDefault",
        "testLoadInitialDataAllowsDuplicateExistingDefault",
    ),
    (
        "remove travel item character guard",
        "TravelList/TravelListItem.swift",
        "guard normalizedName.count <= maximumTravelItemCharacters else",
        "if normalizedName.count <= maximumTravelItemCharacters",
    ),
    (
        "remove travel item length XCTest evidence",
        "TravelListTests/TravelListTests.swift",
        "testTravelItemNameNormalizationEnforcesCharacterLimit",
        "testTravelItemNameNormalizationAllowsUnboundedNames",
    ),
    (
        "remove travel item length documentation",
        "README.md",
        "Travel item names are limited to 100 user-perceived characters after normalization.",
        "Travel item names are normalized.",
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

    print(f"Rejected {len(MUTATIONS)} static contract mutations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
