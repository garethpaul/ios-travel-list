#!/usr/bin/env python3
from pathlib import Path
import json
import plistlib
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
BASELINE_PLAN = ROOT / "docs/plans/2026-06-08-travel-list-baseline.md"
CELL_INDEX_PLAN = ROOT / "docs/plans/2026-06-08-cell-index-guard.md"
CELL_FALLBACK_PLAN = ROOT / "docs/plans/2026-06-08-configurable-cell-fallback.md"
CELL_RESET_PLAN = ROOT / "docs/plans/2026-06-08-fallback-cell-reset.md"
ITEM_NORMALIZER_PLAN = ROOT / "docs/plans/2026-06-09-travel-item-name-normalizer.md"
ITEM_NORMALIZER_TESTS_PLAN = ROOT / "docs/plans/2026-06-09-travel-item-normalizer-tests.md"
ITEM_REMOVAL_PLAN = ROOT / "docs/plans/2026-06-09-travel-item-removal-index-guard.md"
MAKE_GATES_PLAN = ROOT / "docs/plans/2026-06-09-make-gate-aliases.md"
NAV_LOGO_PLAN = ROOT / "docs/plans/2026-06-09-navigation-logo-title-view.md"
TEXTFIELD_GUARD_PLAN = ROOT / "docs/plans/2026-06-10-add-textfield-outlet-guard.md"
CI_WORKFLOW = ROOT / ".github/workflows/check.yml"
CI_PLAN = ROOT / "docs/plans/2026-06-10-ci-baseline.md"
HOSTED_VALIDATION_PLAN = ROOT / "docs/plans/2026-06-10-hosted-project-validation.md"
SWIFT_5_PLAN = ROOT / "docs/plans/2026-06-10-swift-5-typed-list-build.md"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def require(condition, message, failures):
    if not condition:
        failures.append(message)


def read(relative_path):
    return (ROOT / relative_path).read_text(encoding="utf-8", errors="replace")


def strip_swift_line_comments(text):
    return "\n".join(line.split("//", 1)[0] for line in text.splitlines())


def parse_xml(relative_path, failures):
    try:
        ET.parse(str(ROOT / relative_path))
    except ET.ParseError as error:
        failures.append(f"{relative_path} is not well-formed XML: {error}")


def parse_json(relative_path, failures):
    try:
        return json.loads(read(relative_path))
    except json.JSONDecodeError as error:
        failures.append(f"{relative_path} is not valid JSON: {error}")
        return {}


def parse_plist(relative_path, failures):
    try:
        with (ROOT / relative_path).open("rb") as file:
            return plistlib.load(file)
    except Exception as error:
        failures.append(f"{relative_path} is not a readable plist: {error}")
        return {}


def check_png(relative_path, failures):
    path = ROOT / relative_path
    try:
        with path.open("rb") as file:
            signature = file.read(len(PNG_SIGNATURE))
        require(signature == PNG_SIGNATURE, f"{relative_path} must be a PNG image", failures)
        require(path.stat().st_size > 100, f"{relative_path} must not be empty", failures)
    except OSError as error:
        failures.append(f"{relative_path} could not be read: {error}")


def main():
    failures = []
    required_files = [
        ".github/workflows/check.yml",
        ".gitignore",
        ".github/workflows/check.yml",
        "CHANGES.md",
        "Makefile",
        "build.sh",
        "README.md",
        "SECURITY.md",
        "VISION.md",
        "TravelList.xcodeproj/project.pbxproj",
        "TravelList.xcodeproj/project.xcworkspace/contents.xcworkspacedata",
        "TravelList/Info.plist",
        "TravelList/AppDelegate.swift",
        "TravelList/AddTravelViewController.swift",
        "TravelList/TravelListTableViewController.swift",
        "TravelList/TravelListItem.swift",
        "TravelList/Hex.swift",
        "TravelList/Base.lproj/Main.storyboard",
        "TravelList/Images.xcassets/AppIcon.appiconset/Contents.json",
        "TravelList/Images.xcassets/LaunchImage.launchimage/Contents.json",
        "TravelList/Images.xcassets/logoTravel.imageset/Contents.json",
        "TravelList/Images.xcassets/logoTravel.imageset/logoTravel.png",
        "TravelListTests/Info.plist",
        "TravelListTests/TravelListTests.swift",
        "img/app.png",
        "docs/plans/2026-06-08-cell-index-guard.md",
        "docs/plans/2026-06-08-configurable-cell-fallback.md",
        "docs/plans/2026-06-08-fallback-cell-reset.md",
        "docs/plans/2026-06-08-travel-list-baseline.md",
        "docs/plans/2026-06-09-travel-item-name-normalizer.md",
        "docs/plans/2026-06-09-travel-item-normalizer-tests.md",
        "docs/plans/2026-06-09-travel-item-removal-index-guard.md",
        "docs/plans/2026-06-09-make-gate-aliases.md",
        "docs/plans/2026-06-09-navigation-logo-title-view.md",
        "docs/plans/2026-06-10-add-textfield-outlet-guard.md",
        "docs/plans/2026-06-10-ci-baseline.md",
        "docs/plans/2026-06-10-hosted-project-validation.md",
        "docs/plans/2026-06-10-swift-5-typed-list-build.md",
        "docs/readme-overview.svg",
    ]

    for relative_path in required_files:
        require((ROOT / relative_path).is_file(), f"Required file missing: {relative_path}", failures)

    for xml_file in [
        "TravelList.xcodeproj/project.xcworkspace/contents.xcworkspacedata",
        "TravelList/Base.lproj/Main.storyboard",
        "docs/readme-overview.svg",
    ]:
        parse_xml(xml_file, failures)

    for json_file in [
        "TravelList/Images.xcassets/AppIcon.appiconset/Contents.json",
        "TravelList/Images.xcassets/LaunchImage.launchimage/Contents.json",
        "TravelList/Images.xcassets/logoTravel.imageset/Contents.json",
    ]:
        parse_json(json_file, failures)

    for image_file in ["TravelList/Images.xcassets/logoTravel.imageset/logoTravel.png", "img/app.png"]:
        check_png(image_file, failures)

    app_plist = parse_plist("TravelList/Info.plist", failures)
    test_plist = parse_plist("TravelListTests/Info.plist", failures)
    project = read("TravelList.xcodeproj/project.pbxproj")
    storyboard = read("TravelList/Base.lproj/Main.storyboard")
    add_controller = read("TravelList/AddTravelViewController.swift")
    table_controller = read("TravelList/TravelListTableViewController.swift")
    item_model = read("TravelList/TravelListItem.swift")
    tests = read("TravelListTests/TravelListTests.swift")
    swift_sources = "\n".join(strip_swift_line_comments(path.read_text(encoding="utf-8", errors="replace"))
                              for path in sorted((ROOT / "TravelList").glob("*.swift")))
    readme = read("README.md")
    vision = read("VISION.md")
    security = read("SECURITY.md")
    changes = read("CHANGES.md")
    gitignore = read(".gitignore")
    makefile = read("Makefile")
    build_script = read("build.sh")
    baseline_plan = BASELINE_PLAN.read_text(encoding="utf-8") if BASELINE_PLAN.exists() else ""
    cell_index_plan = CELL_INDEX_PLAN.read_text(encoding="utf-8") if CELL_INDEX_PLAN.exists() else ""
    cell_fallback_plan = CELL_FALLBACK_PLAN.read_text(encoding="utf-8") if CELL_FALLBACK_PLAN.exists() else ""
    cell_reset_plan = CELL_RESET_PLAN.read_text(encoding="utf-8") if CELL_RESET_PLAN.exists() else ""
    item_normalizer_plan = ITEM_NORMALIZER_PLAN.read_text(encoding="utf-8") if ITEM_NORMALIZER_PLAN.exists() else ""
    item_normalizer_tests_plan = ITEM_NORMALIZER_TESTS_PLAN.read_text(encoding="utf-8") if ITEM_NORMALIZER_TESTS_PLAN.exists() else ""
    item_removal_plan = ITEM_REMOVAL_PLAN.read_text(encoding="utf-8") if ITEM_REMOVAL_PLAN.exists() else ""
    make_gates_plan = MAKE_GATES_PLAN.read_text(encoding="utf-8") if MAKE_GATES_PLAN.exists() else ""
    nav_logo_plan = NAV_LOGO_PLAN.read_text(encoding="utf-8") if NAV_LOGO_PLAN.exists() else ""
    textfield_guard_plan = TEXTFIELD_GUARD_PLAN.read_text(encoding="utf-8") if TEXTFIELD_GUARD_PLAN.exists() else ""
    ci_workflow = CI_WORKFLOW.read_text(encoding="utf-8") if CI_WORKFLOW.exists() else ""
    ci_plan = CI_PLAN.read_text(encoding="utf-8") if CI_PLAN.exists() else ""
    hosted_validation_plan = HOSTED_VALIDATION_PLAN.read_text(encoding="utf-8") if HOSTED_VALIDATION_PLAN.exists() else ""
    swift_5_plan = SWIFT_5_PLAN.read_text(encoding="utf-8") if SWIFT_5_PLAN.exists() else ""
    workflow = read(".github/workflows/check.yml")

    require(app_plist.get("CFBundleIdentifier", "").startswith("com.garethpaul."),
            "TravelList Info.plist must keep the expected sample bundle identifier",
            failures)
    require(test_plist.get("CFBundlePackageType") == "BNDL",
            "TravelListTests Info.plist must remain a test bundle plist",
            failures)
    require(project.count("IPHONEOS_DEPLOYMENT_TARGET = 12.0;") == 2 and
            project.count("SWIFT_VERSION = 5.0;") == 4 and
            'INFOPLIST_FILE = "$(SRCROOT)/TravelList/Info.plist";' in project,
            "Xcode project must use Swift 5 and iOS 12 while preserving Info.plist wiring",
            failures)
    require("ENABLE_TESTABILITY = YES;" in project and "@testable import TravelList" in tests,
            "Xcode project and tests must keep TravelList app code testable from XCTest",
            failures)
    require("Images.xcassets" in project and "Main.storyboard" in project,
            "Xcode project must keep storyboard and image asset references",
            failures)
    require("TravelListTableViewController" in storyboard and "AddTravelViewController" in storyboard and "unwindToList" in storyboard,
            "Storyboard must keep the list/add/unwind flow wired",
            failures)
    require("TravelListItem.normalizedName(textfield.text)" in add_controller,
            "AddTravelViewController must normalize item names before accepting them",
            failures)
    for controller_name, controller_source in {
        "TravelListTableViewController": table_controller,
        "AddTravelViewController": add_controller,
    }.items():
        require("navigationItem.titleView = logoView" in controller_source and
                "navigationController?.view.addSubview(logoView)" not in controller_source and
                "bringSubviewToFront(logoView)" not in controller_source and
                "logoView.frame.origin" not in controller_source,
                f"{controller_name} must scope the travel logo to the navigation item title view",
                failures)
    require("class func normalizedName(_ name: String?) -> String?" in item_model and
            "trimmingCharacters(in: .whitespacesAndNewlines)" in item_model and
            "itemName.isEmpty" in item_model and "return nil" in item_model,
            "TravelListItem must expose a shared optional name normalizer",
            failures)
    require("testTravelItemNameNormalizationTrimsWhitespace" in tests and
            "testTravelItemNameNormalizationRejectsBlankNames" in tests and
            "testRemoveTravelItemAtIndexRemovesValidItem" in tests and
            "testRemoveTravelItemAtIndexRejectsInvalidIndexes" in tests and
            "XCTAssertEqual" in tests and "XCTAssertNil" in tests and
            "XCTAssert(true" not in tests and "testPerformanceExample" not in tests,
            "TravelListTests must replace template tests with travel item normalization and removal assertions",
            failures)
    require("travelItem = nil" in add_controller and "let textfield = textfield" in add_controller and
            "TravelListItem.normalizedName(textfield.text)" in add_controller,
            "AddTravelViewController must avoid force-unwrapping text and clear stale pending items",
            failures)
    require("!itemName.isEmpty" in item_model and "TravelListItem(name: itemName)" in add_controller,
            "AddTravelViewController must reject whitespace-only items",
            failures)
    hex_source = read("TravelList/Hex.swift")
    require("UInt32(value, radix: 16)" in hex_source and "value.count == 6" in hex_source,
            "Hex parser must reject malformed values",
            failures)
    require("as? AddTravelViewController" in table_controller and "var travelItems: [TravelListItem] = []" in table_controller and
            "NSMutableArray" not in swift_sources,
            "TravelListTableViewController must guard the storyboard cast and use typed item storage",
            failures)
    require("?? UITableViewCell(style: .default" in table_controller and "return UITableViewCell()" not in table_controller and
            "travelItems.indices.contains(indexPath.row)" in table_controller,
            "TravelListTableViewController must use a configurable fallback cell and guard invalid delete indexes",
            failures)
    require("func removeTravelItem(at index: Int) -> Bool" in table_controller and
            "travelItems.indices.contains(index)" in table_controller and
            "travelItems.remove(at: index)" in table_controller and
            "if removeTravelItem(at: indexPath.row)" in table_controller,
            "TravelListTableViewController must remove items through a guarded index helper",
            failures)
    require("func configureCell(_ cell: UITableViewCell, with travelItem: TravelListItem?) -> UITableViewCell" in table_controller and
            'cell.textLabel?.text = ""' in table_controller and
            "return configureCell(cell, with: nil)" in table_controller and
            "return configureCell(cell, with: travelItems[indexPath.row])" in table_controller,
            "TravelListTableViewController must clear fallback cells before returning invalid or malformed rows",
            failures)
    cell_method = table_controller.split("cellForRowAt indexPath", 1)[1].split("didSelectRowAt indexPath", 1)[0]
    require("travelItems.indices.contains(indexPath.row)" in cell_method and
            "return configureCell(cell, with: nil)" in cell_method,
            "cellForRowAtIndexPath must guard invalid indexes before reading travelItems",
            failures)
    require("reloadData" not in cell_method,
            "cellForRowAtIndexPath must not reload the table while rendering cells",
            failures)
    require("loadInitialData" in table_controller and "Phone" in table_controller and "Wallet" in table_controller and "Passport" in table_controller,
            "TravelListTableViewController must keep the sample seed items",
            failures)
    require("final class TravelListItem" in item_model and "creationDate" in item_model,
            "TravelListItem model must keep name/completion/date fields",
            failures)
    require(not re.search(r"\b(?:print|println|NSLog)\s*\(", swift_sources),
            "Travel-list data must not be debug logged",
            failures)
    require("as!" not in swift_sources and "text!" not in swift_sources,
            "Travel-list sources must avoid force-casts and force-unwrapped text fields",
            failures)
    for forbidden in ["NSURL", "URLSession", "NSURLConnection", "http://", "https://", "upload", "analytics", "NSUserDefaults", "UserDefaults"]:
        require(forbidden not in swift_sources,
                f"Travel-list sample must not add network, upload, analytics, or persistence behavior: {forbidden}",
                failures)

    swift_files = sorted((ROOT / "TravelList").glob("*.swift")) + sorted((ROOT / "TravelListTests").glob("*.swift"))
    require(len(swift_files) >= 6,
            "expected Swift source/test inventory is missing",
            failures)
    require(".PHONY: build check lint test" in makefile and "lint test build: check" in makefile and
            "check:\n\tpython3 scripts/check-baseline.py\n\t./build.sh" in makefile,
            "Makefile must expose lint, test, build, and check verification gates",
            failures)
    shell_result = subprocess.run(["sh", "-n", "build.sh"], cwd=str(ROOT), text=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    require(shell_result.returncode == 0 and 'xcodebuild -project "TravelList.xcodeproj"' in build_script and
            '-target "TravelList"' in build_script and "CODE_SIGNING_ALLOWED=NO" in build_script and
            "xcodebuild unavailable" in build_script,
            "build.sh must compile the unsigned TravelList simulator target and skip cleanly without Xcode",
            failures)
    require("*.local.xcconfig" in gitignore and ".env" in gitignore and "DerivedData" in gitignore,
            ".gitignore must exclude local config and Xcode build products",
            failures)
    require("make lint" in readme and "make test" in readme and "make build" in readme and
            "make check" in readme and "GitHub Actions" in readme and "TravelList.xcodeproj" in readme and "local-first" in readme.lower(),
            "README must document static verification gates, project usage, and local-first behavior",
            failures)
    require("whitespace" in readme.lower() and "cell rendering" in readme.lower() and "index" in readme.lower() and
            "color fallback" in readme.lower() and "fallback cell" in readme.lower() and "stale cell" in readme.lower() and
            "textfield outlet" in readme.lower() and "name normalizer" in readme.lower() and "title view" in readme.lower(),
            "README must document item trimming, cell rendering, fallback cell reset, index, and parser guardrails",
            failures)
    require("normalizer tests" in readme.lower(),
            "README must document travel item normalizer tests",
            failures)
    require("removal index" in readme.lower(),
            "README must document travel item removal index guardrails",
            failures)
    require("scripts/check-baseline.py" in vision and "make lint" in vision and "make test" in vision and
            "make build" in vision and "GitHub Actions" in vision and "local-first" in vision.lower() and
            "fallback cell" in vision.lower() and "stale cell" in vision.lower() and
            "textfield outlet" in vision.lower() and "name normalizer" in vision.lower() and "title view" in vision.lower(),
            "VISION must describe the current static travel-list baseline",
            failures)
    require("normalizer tests" in vision.lower(),
            "VISION must describe travel item normalizer tests",
            failures)
    require("removal index" in vision.lower(),
            "VISION must describe travel item removal index guardrails",
            failures)
    require("travel lists" in security.lower() and "make check" in security and "GitHub Actions" in security and "stale cell" in security.lower() and
            "name normalizer" in security.lower() and "normalizer tests" in security.lower() and
            "textfield outlet" in security.lower() and "removal index" in security.lower() and "title view" in security.lower(),
            "SECURITY must document travel-list privacy and the static baseline",
            failures)
    require("GitHub Actions" in changes and "whitespace-only" in changes and "hex color" in changes and "cell rendering" in changes and
            "fallback cell" in changes.lower() and "stale cell" in changes.lower() and "title view" in changes.lower() and
            "index" in changes.lower() and "textfield outlet" in changes.lower() and "name normalizer" in changes.lower() and "make check" in changes,
            "CHANGES must record item trimming, parser hardening, cell rendering/index cleanup, fallback cell reset, and baseline",
            failures)
    require("make lint" in changes and "make test" in changes and "make build" in changes,
            "CHANGES must record the standard local gate aliases",
            failures)
    require("normalizer tests" in changes.lower(),
            "CHANGES must record travel item normalizer test updates",
            failures)
    require("removal index" in changes.lower(),
            "CHANGES must record travel item removal index updates",
            failures)
    require("status: completed" in baseline_plan and "status: completed" in cell_index_plan and
            "status: completed" in cell_fallback_plan and "status: completed" in cell_reset_plan,
            "plans must be marked completed",
            failures)
    require("status: completed" in item_normalizer_plan,
            "travel item name normalizer plan must be marked completed",
            failures)
    require("status: completed" in item_normalizer_tests_plan,
            "travel item normalizer tests plan must be marked completed",
            failures)
    require("status: completed" in item_removal_plan,
            "travel item removal index guard plan must be marked completed",
            failures)
    require("status: completed" in make_gates_plan,
            "make gate aliases plan must be marked completed",
            failures)
    require("status: completed" in nav_logo_plan,
            "navigation logo title-view plan must be marked completed",
            failures)
    require("status: completed" in textfield_guard_plan,
            "add textfield outlet guard plan must be marked completed",
            failures)
    require("status: completed" in ci_plan and "GitHub Actions" in ci_plan and "make check" in ci_plan,
            "CI baseline plan must record hosted make check verification",
            failures)
    require("status: completed" in hosted_validation_plan and "make check" in hosted_validation_plan,
            "hosted validation plan must be completed", failures)
    require("status: completed" in swift_5_plan and "XCTest source remains non-executable" in swift_5_plan,
            "Swift 5 typed-list plan must be completed and document the test-target boundary", failures)
    checkout_step = re.search(
        r"(?m)^      - name: Check out repository\n"
        r"        uses: actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10 # v6\.0\.3\n"
        r"        with:\n"
        r"          persist-credentials: false\n",
        workflow,
    )
    require(checkout_step is not None and
            workflow.count("actions/checkout@") == 1 and
            workflow.count("persist-credentials:") == 1 and
            "permissions:\n  contents: read" in workflow and "cancel-in-progress: true" in workflow and
            "runs-on: macos-15" in workflow and "timeout-minutes: 10" in workflow and
            "actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10" in workflow and "run: make check" in workflow,
            "Check workflow contract must stay singular, pinned, credential-free, read-only, and bounded", failures)

    if shutil.which("xcodebuild"):
        result = subprocess.run(["xcodebuild", "-list", "-project", "TravelList.xcodeproj"], cwd=ROOT,
                                stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        require(result.returncode == 0,
                "xcodebuild could not parse TravelList.xcodeproj: " + result.stderr.strip(), failures)
    else:
        print("xcodebuild unavailable; static iOS baseline only.")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    print("ios-travel-list baseline checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
