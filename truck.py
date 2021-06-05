import datetime


class Truck:
    def __init__(self, current_address):
        self.location = current_address
        self.packages = []
        self.start_time = datetime.time(7)  # when the truck leaves the hub to deliver the first package
        self.speed = 18  # miles per hour

    def add_package(self, nextpackage):
        self.packages.append(nextpackage)

    def get_delivery_time(self, packageid):
        time_delivered = datetime.timedelta()

        for item in self.packages:
            distance = self.calculate_distance(self.location, item.address)

            print(self.location + " is " + distance + " miles from address: " + item.address)

            time_delivered = time_delivered + datetime.timedelta(seconds=distance / self.speed)
            if item.packageID == packageid:
                break

        return time_delivered + self.start_time

    def deliver(self):
        for item in self.packages:
            self.calculate_distance(item)

    def calculate_distance(thisAddress, nextAddress):
        return 1
