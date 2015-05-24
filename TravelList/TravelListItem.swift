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

}
