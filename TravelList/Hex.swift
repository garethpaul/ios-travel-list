import UIKit

func toColor(_ hex: String) -> UIColor {
    var value = hex.trimmingCharacters(in: .whitespacesAndNewlines).uppercased()
    if value.hasPrefix("#") {
        value.removeFirst()
    }

    guard value.count == 6,
          let rgbValue = UInt32(value, radix: 16) else {
        return .gray
    }

    return UIColor(
        red: CGFloat((rgbValue & 0xFF0000) >> 16) / 255,
        green: CGFloat((rgbValue & 0x00FF00) >> 8) / 255,
        blue: CGFloat(rgbValue & 0x0000FF) / 255,
        alpha: 1
    )
}
