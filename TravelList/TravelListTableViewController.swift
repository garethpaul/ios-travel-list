//
//  TableViewController.swift
//

import UIKit

class TravelListTableViewController: UITableViewController {

    @IBAction func unwindToList(segue:UIStoryboardSegue){
        let source: AddTravelViewController = segue.sourceViewController as! AddTravelViewController
        if let item: TravelListItem = source.travelItem{
            self.travelItems.addObject(item)
            self.tableView.reloadData()
        }
        
    }
    
    var travelItems: NSMutableArray = []
    var logoView: UIImageView!
    
    override func viewDidLoad(){
        super.viewDidLoad()
        self.tableView.tableFooterView = UIView(frame: CGRectZero)
        self.tableView.contentInset = UIEdgeInsets(top: 0, left: -10, bottom: 0, right: 0)
        
        logoView = UIImageView(frame: CGRectMake(0, 0, 40, 40))
        logoView.image = UIImage(named: "logoTravel")?.imageWithRenderingMode(.AlwaysTemplate)
        logoView.frame.origin.x = (self.view.frame.size.width - logoView.frame.size.width) / 2
        logoView.frame.origin.y = 20
        logoView.tintColor = toColor("#F9F9F9")
        
        // Add the logo view to the navigation controller.
        self.navigationController?.view.addSubview(logoView)
        
        // Bring the logo view to the front.
        self.navigationController?.view.bringSubviewToFront(logoView)
        
        loadInitialData()
    }
    
    func loadInitialData(){
        let item1 = TravelListItem(name:"Phone")
        self.travelItems.addObject(item1)
        let item2 = TravelListItem(name: "Wallet")
        self.travelItems.addObject(item2)
        let item3 = TravelListItem(name: "Passport")
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
        
        let cell : UITableViewCell = tableView.dequeueReusableCellWithIdentifier(CellIndentifier as String)!
        
        let travelItem = self.travelItems.objectAtIndex(indexPath.row) as! TravelListItem
        
        cell.textLabel?.text = travelItem.itemName as String
        cell.textLabel?.textColor = UIColor.whiteColor()

        
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
        self.travelItems.removeObjectAtIndex(indexPath.row)
        tableView.reloadData()
        
    }
}









