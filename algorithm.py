from packagehashtable import PackageHashTable
from truck import Truck
from package import Package
import distancegraph


def load_trucks(truck1: Truck, truck2: Truck, truck3: Truck, packages: PackageHashTable):
    packages.get_package(9).address = "410 S State St"

    # truck1_packages = [3, 8, 30, 5, 9, 37, 38, 10, 13, 39, 1, 28, 2, 27, 33, 35]
    # truck2_packages = [7, 29, 4, 40, 20, 21, 31, 32, 12]
    # truck3_packages = [19, 6, 36, 17, 24, 14, 25, 26, 15, 16, 34, 18, 23, 11, 22]

    truck1_packages = [3, 8, 30, 5, 9, 37, 38, 10, 13, 39, 1, 28, 2, 27, 33, 35]
    truck2_packages = [7, 29, 4, 40, 20, 21, 31, 32, 12]
    truck3_packages = [19, 6, 36, 17, 24, 14, 25, 26, 15, 16, 34, 18, 23, 11, 22]

    truck1_packages.reverse()

    for item in truck1_packages:
        truck1.add_package(packages.get_package(item))
    truck1.add_package(Package(0, "4001 South 700 East", "", "", "", "", ""))
    for item in truck2_packages:
        truck2.add_package(packages.get_package(item))
    for item in truck3_packages:
        truck3.add_package(packages.get_package(item))


class NearestNeighbor:
    def __init__(self, graph: distancegraph.Distance, packages: PackageHashTable):
        self.graph = graph
        self.hub_address = "233 Canyon Rd"
        self.current_address = "233 Canyon Rd"
        self.final_route = []
        self.packages_left = []
        for x in range(1, packages.get_filled_slots() + 1):
            if x == 9:
                packages.get_package(x).address = "410 S State St"

            self.packages_left.append(packages.get_package(x))

    def greedy_sort(self):
        current_address = self.hub_address

        while self.packages_left.__len__() > 0:
            # find next package closest to hub
            # add package to list
            self.final_route.append(self.pop_nearest_package())

        temp_string = ""
        for x in self.final_route:
            temp_string += str(x.package_id) + ", "
        print(temp_string)

    def pop_nearest_package(self):
        # iterate through all possible packages
        temporary_package = []
        for item in self.packages_left:
            distance = self.graph.get_distance_from_location_to_locations(self.current_address,
                                                                          item.address)
            if temporary_package.__len__() == 0:
                temporary_package.append(item)
                temporary_package.append(distance)
            elif temporary_package[1] > distance:
                temporary_package.clear()
                temporary_package.append(item)
                temporary_package.append(distance)

        self.packages_left.remove(temporary_package[0])
        return temporary_package[0]
