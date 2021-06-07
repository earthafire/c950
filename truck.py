import datetime
import distancegraph


class Truck:
    def __init__(self, current_address, distance_map: distancegraph):
        self.location = current_address
        self.packages = []
        self.start_time = datetime.timedelta(hours= 7)  # when the truck leaves the hub to deliver the first package
        self.speed = 18  # miles per hour
        self.distance_map = distance_map

    def add_package(self, package):
        self.packages.append(package)

    def get_delivery_time(self, package_id):
        time_delivered = datetime.timedelta()

        for item in self.packages:
            distance = self.calculate_distance(self.location, item.address)

            print(self.location + " is " + distance + " miles from address: " + item.address)

            time_delivered = time_delivered + datetime.timedelta(seconds=distance / self.speed)
            if item.packageID == package_id:
                break

        return self.start_time + time_delivered

    def view_cargo(self):
        for item in self.packages:
            item.print()

    def deliver(self):
        distance = 0

        # deliver all packages
        for item in self.packages:
            print("Next stop: " + item.address)
            distance += self.distance_map.get_distance_from_location_to_locations(self.location, item.address)
            self.location = item.address
            item.status = "delivered"

        # return to hub
        self.distance_map.get_distance_from_location_to_locations(self.location, "4001 South 700 East")
        print("Total distance %3.1f" % distance)
