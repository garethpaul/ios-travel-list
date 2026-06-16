//
//  MyAppTests.swift
//  MyAppTests
//

import XCTest
@testable import TravelList

final class MyAppTests: XCTestCase {

    func testTravelItemNameNormalizationTrimsWhitespace() {
        XCTAssertEqual(TravelListItem.normalizedName("  Passport\n"), "Passport", "Travel item names should be trimmed before saving")
    }

    func testTravelItemNameNormalizationRejectsBlankNames() {
        XCTAssertNil(TravelListItem.normalizedName("  \n\t  "), "Blank travel item names should be ignored")
        XCTAssertNil(TravelListItem.normalizedName(nil), "Missing travel item names should be ignored")
    }

    func testTravelItemNameNormalizationRejectsEmbeddedControlCharacters() {
        XCTAssertNil(TravelListItem.normalizedName("Pass\nport"))
        XCTAssertNil(TravelListItem.normalizedName("Pass\tport"))
        XCTAssertNil(TravelListItem.normalizedName("Pass\u{0}port"))
    }

    func testTravelItemNameNormalizationPreservesInternationalizedNames() {
        XCTAssertEqual(TravelListItem.normalizedName("  Café Guide  "), "Café Guide")
    }

    func testRemoveTravelItemAtIndexRemovesValidItem() {
        let controller = TravelListTableViewController()
        controller.travelItems.append(TravelListItem(name: "Passport"))

        XCTAssertTrue(controller.removeTravelItem(at: 0), "Valid travel item indexes should be removable")
        XCTAssertEqual(controller.travelItems.count, 0, "Removing a valid item should update the local list")
    }

    func testRemoveTravelItemAtIndexRejectsInvalidIndexes() {
        let controller = TravelListTableViewController()
        controller.travelItems.append(TravelListItem(name: "Passport"))

        XCTAssertFalse(controller.removeTravelItem(at: -1), "Negative travel item indexes should not be removed")
        XCTAssertFalse(controller.removeTravelItem(at: 1), "Out-of-range travel item indexes should not be removed")
        XCTAssertEqual(controller.travelItems.count, 1, "Invalid item removal should leave the local list unchanged")
    }

    func testAddTravelItemAppendsUniqueItem() {
        let controller = TravelListTableViewController()

        XCTAssertTrue(controller.addTravelItem(TravelListItem(name: "  Passport\n")))
        XCTAssertEqual(controller.travelItems.count, 1)
        XCTAssertEqual(controller.travelItems.first?.itemName, "Passport")
    }

    func testAddTravelItemRejectsCaseInsensitiveDuplicates() {
        let controller = TravelListTableViewController()
        controller.travelItems.append(TravelListItem(name: "Passport"))

        XCTAssertFalse(controller.addTravelItem(TravelListItem(name: "Passport")))
        XCTAssertFalse(controller.addTravelItem(TravelListItem(name: "passport")))
        XCTAssertFalse(controller.addTravelItem(TravelListItem(name: "  PASSPORT\n")))
        XCTAssertEqual(controller.travelItems.count, 1)
    }

    func testAddTravelItemRejectsDuplicateOfNoncanonicalExistingItem() {
        let controller = TravelListTableViewController()
        let existingItem = TravelListItem(name: "  Passport\n")
        controller.travelItems.append(existingItem)

        XCTAssertFalse(controller.addTravelItem(TravelListItem(name: "passport")))
        XCTAssertEqual(controller.travelItems.count, 1)
        XCTAssertEqual(existingItem.itemName, "  Passport\n")
    }

    func testAddTravelItemRejectsBlankDirectCaller() {
        let controller = TravelListTableViewController()

        XCTAssertFalse(controller.addTravelItem(TravelListItem(name: "  \n\t  ")))
        XCTAssertTrue(controller.travelItems.isEmpty)
    }

}
