import UIKit

class AddTravelViewController: UIViewController {
    var travelItem: TravelListItem?

    @IBOutlet private var textfield: UITextField!
    @IBOutlet private var doneButton: UIBarButtonItem!

    override func viewDidLoad() {
        super.viewDidLoad()

        let logoView = UIImageView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
        logoView.image = UIImage(named: "logoTravel")?.withRenderingMode(.alwaysTemplate)
        logoView.tintColor = toColor("#F9F9F9")
        navigationItem.titleView = logoView
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        travelItem = nil
        guard sender as AnyObject? === doneButton,
              let textfield = textfield,
              let itemName = TravelListItem.normalizedName(textfield.text) else {
            return
        }

        travelItem = TravelListItem(name: itemName)
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        view.endEditing(true)
    }
}
