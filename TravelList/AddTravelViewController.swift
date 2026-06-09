//
//  ViewController.swift
//

import UIKit

class AddTravelViewController: UIViewController {
    
    var travelItem: TravelListItem?

    @IBOutlet var textfield : UITextField!
    @IBOutlet var doneButton : UIBarButtonItem!
    var logoView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        logoView = UIImageView(frame: CGRectMake(0, 0, 40, 40))
        logoView.image = UIImage(named: "logoTravel")?.imageWithRenderingMode(.AlwaysTemplate)
        logoView.tintColor = toColor("#F9F9F9")
        self.navigationItem.titleView = logoView
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        self.travelItem = nil
        if sender as? NSObject != self.doneButton{
            return
        }
        if let itemName = TravelListItem.normalizedName(self.textfield.text) {
            self.travelItem = TravelListItem(name: itemName)
        }
    }
    
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
        self.view.endEditing(true)
    }


}
