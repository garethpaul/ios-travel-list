import Foundation

final class TravelListItem: NSObject {
    var itemName: String
    var completed = false
    let creationDate = Date()

    init(name: String) {
        itemName = name
        super.init()
    }

    class func normalizedName(_ name: String?) -> String? {
        guard let itemName = name?.trimmingCharacters(in: .whitespacesAndNewlines),
              !itemName.isEmpty else {
            return nil
        }

        guard itemName.rangeOfCharacter(from: .controlCharacters) == nil else {
            return nil
        }

        guard itemName.rangeOfCharacter(from: .newlines) == nil else {
            return nil
        }

        return itemName.components(separatedBy: .whitespaces)
            .filter { !$0.isEmpty }
            .joined(separator: " ")
    }

    class func duplicateKey(forNormalizedName name: String) -> String {
        name.folding(options: [.caseInsensitive, .widthInsensitive],
                     locale: Locale(identifier: "en_US_POSIX"))
            .precomposedStringWithCanonicalMapping
    }
}
