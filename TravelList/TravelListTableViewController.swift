import UIKit

class TravelListTableViewController: UITableViewController {
    var travelItems: [TravelListItem] = []

    @IBAction func unwindToList(_ segue: UIStoryboardSegue) {
        guard let source = segue.source as? AddTravelViewController,
              let item = source.travelItem else {
            return
        }

        if addTravelItem(item) {
            tableView.reloadData()
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.tableFooterView = UIView(frame: .zero)
        tableView.contentInset = UIEdgeInsets(top: 0, left: -10, bottom: 0, right: 0)

        let logoView = UIImageView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
        logoView.image = UIImage(named: "logoTravel")?.withRenderingMode(.alwaysTemplate)
        logoView.tintColor = toColor("#F9F9F9")
        navigationItem.titleView = logoView

        loadInitialData()
    }

    func loadInitialData() {
        travelItems.append(TravelListItem(name: "Phone"))
        travelItems.append(TravelListItem(name: "Wallet"))
        travelItems.append(TravelListItem(name: "Passport"))
    }

    override func numberOfSections(in tableView: UITableView) -> Int {
        1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        travelItems.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let reuseIdentifier = "ListPrototypeCell"
        let cell = tableView.dequeueReusableCell(withIdentifier: reuseIdentifier)
            ?? UITableViewCell(style: .default, reuseIdentifier: reuseIdentifier)

        guard travelItems.indices.contains(indexPath.row) else {
            return configureCell(cell, with: nil)
        }

        return configureCell(cell, with: travelItems[indexPath.row])
    }

    func configureCell(_ cell: UITableViewCell, with travelItem: TravelListItem?) -> UITableViewCell {
        guard let travelItem = travelItem else {
            cell.textLabel?.text = ""
            cell.textLabel?.textColor = .white
            cell.accessoryType = .none
            return cell
        }

        cell.textLabel?.text = travelItem.itemName
        cell.textLabel?.textColor = .white
        cell.accessoryType = travelItem.completed ? .checkmark : .none
        return cell
    }

    func removeTravelItem(at index: Int) -> Bool {
        guard travelItems.indices.contains(index) else {
            return false
        }

        travelItems.remove(at: index)
        return true
    }

    func addTravelItem(_ item: TravelListItem) -> Bool {
        guard !travelItems.contains(where: {
            $0.itemName.caseInsensitiveCompare(item.itemName) == .orderedSame
        }) else {
            return false
        }

        travelItems.append(item)
        return true
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: false)
        if removeTravelItem(at: indexPath.row) {
            tableView.reloadData()
        }
    }
}
