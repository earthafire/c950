class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = "at the hub"  # all packages start at the hub when read in

    def print(self):
        print("Package ID: {0}\t - Address: {1} - Deadline: {2} - City: {3} - Zip: {4} - Weight: {5} - Status: {6}"
              .format(self.package_id, self.address, self.deadline, self.city, self.zipcode, self.weight, self.status))
