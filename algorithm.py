from packagehashtable import PackageHashTable
from truck import Truck
from package import Package
import distancegraph


def load_trucks(truck1: Truck, truck2: Truck, truck3: Truck, packages: PackageHashTable):
    packages.get_package(9).address = "410 S State St"

    truck1_packages = [2, 33, 1, 4, 40, 7, 29, 10, 5, 37, 38, 8, 30]
    truck2_packages = [14, 16, 15, 24, 20, 21, 19, 12, 36, 6, 17, 31, 18, 13, 3, 22]
    truck3_packages = [25, 26, 34, 28, 32, 27, 35, 39, 9, 23, 11]

    truck1_packages.reverse()

    for item in truck1_packages:
        truck1.add_package(packages.get_package(item))
    truck1.add_package(Package(0, "4001 South 700 East", "", "", "", "", ""))
    for item in truck2_packages:
        truck2.add_package(packages.get_package(item))
    truck2.add_package(Package(0, "4001 South 700 East", "", "", "", "", ""))
    for item in truck3_packages:
        truck3.add_package(packages.get_package(item))
    truck3.add_package(Package(0, "4001 South 700 East", "", "", "", "", ""))


class NearestNeighbor:
    def __init__(self, graph: distancegraph.Distance):
        self.graph = graph
        self.hub_address = "4001 South 700 East"
        self.current_address = "4001 South 700 East"

    def greedy_sort(self, package_list):
        self.current_address = self.hub_address
        final_route = []
        while package_list.__len__() > 0:
            # find next package closest to hub and add it to the list
            final_route.append(self.pop_nearest_package(package_list))

        # print out answer so user can see
        temp_string = ""
        for x in final_route:
            temp_string += str(x.package_id) + ", "
        print(temp_string)

    def pop_nearest_package(self, package_list):
        # iterate through all possible packages
        temporary_package = []
        for item in package_list:
            distance = self.graph.get_distance_from_location_to_locations(self.current_address,
                                                                          item.address)
            # save package if none saved yet, or replace package if it is closer than the saved package
            if temporary_package.__len__() == 0:
                temporary_package.append(item)
                temporary_package.append(distance)
            elif temporary_package[1] > distance:
                temporary_package.clear()
                temporary_package.append(item)
                temporary_package.append(distance)

        # pop the closest package and return it
        package_list.remove(temporary_package[0])
        self.current_address = temporary_package[0].address
        return temporary_package[0]
