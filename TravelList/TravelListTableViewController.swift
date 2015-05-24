//
//  TableViewController.swift
//

import UIKit

class TravelListTableViewController: UITableViewController {

    @IBAction func unwindToList(segue:UIStoryboardSegue){
        var source: AddTravelViewController = segue.sourceViewController as! AddTravelViewController
        if var item: TravelListItem = source.travelItem{
            self.travelItems.addObject(item)
            self.tableView.reloadData()
        }
        
    }
    
    var travelItems: NSMutableArray = []

    
    override func viewDidLoad(){
        super.viewDidLoad()
        loadInitialData()
    }
    
    func loadInitialData(){
        var item1 = TravelListItem(name:"Phone")
        self.travelItems.addObject(item1)
        var item2 = TravelListItem(name: "Wallet")
        self.travelItems.addObject(item2)
        var item3 = TravelListItem(name: "Passport")
        self.travelItems.addObject(item3)
    }
    
    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.travelItems.count
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let CellIndentifier: NSString = "ListPrototypeCell"
        
        var cell : UITableViewCell = tableView.dequeueReusableCellWithIdentifier(CellIndentifier as String) as! UITableViewCell
        
        var travelItem = self.travelItems.objectAtIndex(indexPath.row) as! TravelListItem
        
        cell.textLabel?.text = travelItem.itemName as String
        
        if travelItem.completed{
            cell.accessoryType = .Checkmark

            tableView.reloadData()

        }
            
        else{
            
            cell.accessoryType = .None
            
        }
        
        return cell
    }
    
    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        tableView.deselectRowAtIndexPath(indexPath, animated: false)
        var tappedItem: TravelListItem = self.travelItems.objectAtIndex(indexPath.row) as! TravelListItem
        self.travelItems.removeObjectAtIndex(indexPath.row)
        tableView.reloadData()
        
    }
}









