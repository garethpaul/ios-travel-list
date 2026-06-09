//
//  MyAppTests.swift
//  MyAppTests
//

import XCTest
@testable import TravelList

class MyAppTests: XCTestCase {

    func testTravelItemNameNormalizationTrimsWhitespace() {
        XCTAssertEqual(TravelListItem.normalizedName("  Passport\n")!, "Passport", "Travel item names should be trimmed before saving")
    }

    func testTravelItemNameNormalizationRejectsBlankNames() {
        XCTAssertNil(TravelListItem.normalizedName("  \n\t  "), "Blank travel item names should be ignored")
        XCTAssertNil(TravelListItem.normalizedName(nil), "Missing travel item names should be ignored")
    }

}
