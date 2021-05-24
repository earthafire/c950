import datetime


class Truck:
    def __init__(self, current_address):
        self.location = current_address
        self.packages = []
        self.start_time = datetime.time()
        self.start_time.hour = 7  # when the truck leaves the hub to deliver the first package
        self.speed = 18  # miles per hour

    def add_package(self, nextpackage):
        self.packages.append(nextpackage)

    def get_delivery_time(self, packageID):
        time_delivering = datetime.time()

        for item in self.packages:
            time_delivering += self.calculate_distance(self.location, item.address)
            if item.packageID == packageID:
                break

        return time_delivering + self.start_time

    def deliver(self):
        for item in self.packages:
            self.calculate_distance(item)

    def calculate_distance(thisAddress, nextAddress):
        return 1
