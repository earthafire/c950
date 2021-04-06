class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = "at the hub"  # all packages start at the hub when read in
