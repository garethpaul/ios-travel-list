//
//  ToDoItem.swift

import Foundation

class TravelListItem: NSObject{

    var itemName: NSString = ""
    var completed: Bool = false
    var creationDate: NSDate = NSDate()
    
    init(name:String){
        self.itemName = name
    }

    class func normalizedName(name: String?) -> String? {
        if let itemName = name?.stringByTrimmingCharactersInSet(NSCharacterSet.whitespaceAndNewlineCharacterSet()) where !itemName.isEmpty {
            return itemName
        }

        return nil
    }

}
