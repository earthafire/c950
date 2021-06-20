from packagehashtable import PackageHashTable
from truck import Truck
from package import Package
import distancegraph


def load_trucks(truck1: Truck, truck2: Truck, truck3: Truck, packages: PackageHashTable):
    truck1.add_package(packages.get_package(14))
    truck1.add_package(packages.get_package(20))
    truck1.add_package(packages.get_package(21))
    truck1.add_package(packages.get_package(19))
    truck1.add_package(packages.get_package(24))
    truck1.add_package(packages.get_package(25))
    truck1.add_package(packages.get_package(26))
    truck1.add_package(packages.get_package(2))
    truck1.add_package(packages.get_package(33))
    truck1.add_package(packages.get_package(28))
    truck1.add_package(packages.get_package(15))
    truck1.add_package(packages.get_package(16))
    truck1.add_package(packages.get_package(34))
    truck1.add_package(packages.get_package(1))
    truck1.add_package(packages.get_package(4))
    truck1.add_package(packages.get_package(22))
    # this package sends the truck back to hub for more packages, not a real package
    truck1.add_package(Package(0, "4001 South 700 East", "", "", "", "", ""))

    truck2.add_package(packages.get_package(40))
    truck2.add_package(packages.get_package(31))
    truck2.add_package(packages.get_package(32))
    truck2.add_package(packages.get_package(7))
    truck2.add_package(packages.get_package(29))
    truck2.add_package(packages.get_package(17))
    truck2.add_package(packages.get_package(10))
    truck2.add_package(packages.get_package(6))
    truck2.add_package(packages.get_package(11))
    truck2.add_package(packages.get_package(23))
    truck2.add_package(packages.get_package(5))
    truck2.add_package(packages.get_package(37))
    truck2.add_package(packages.get_package(38))
    truck2.add_package(packages.get_package(27))
    truck2.add_package(packages.get_package(35))
    truck2.add_package(packages.get_package(3))

    truck3.add_package(packages.get_package(8))
    truck3.add_package(packages.get_package(9))
    truck3.add_package(packages.get_package(12))
    truck3.add_package(packages.get_package(30))
    truck3.add_package(packages.get_package(36))
    truck3.add_package(packages.get_package(13))
    truck3.add_package(packages.get_package(39))
    truck3.add_package(packages.get_package(18))


class NearestNeighbor:
    def __init__(self, graph: distancegraph.Distance, packages: PackageHashTable):
        self.graph = graph
        self.hub_address = "4001 South 700 East"
        self.current_address = "4001 South 700 East"
        self.final_route = []
        self.packages_left = []
        for x in range(1, packages.get_filled_slots() + 1):
            self.packages_left.append(packages.get_package(x))

    def greedy_sort(self):
        current_address = self.hub_address

        while self.packages_left.__len__() > 0:
            # find next package closest to hub
            # add package to list
            self.final_route.append(self.pop_nearest_package())

        for x in self.final_route:
            print(x.package_id)

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
