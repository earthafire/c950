# Addison Ashworth C950


import truck
import packagehashtable
from excelpackagedataimporter import *
from distancegraph import Distance

# beginning of program
if __name__ == '__main__':
    packages = packagehashtable.PackageHashTable()
    packages = get_packages_from_file("WGUPS Package File.csv")
    # TODO:load packages into trucks
    #
    # print("Make a selection")
    # print("0 look up package id")
    # print("1 look up packages at time")
    # val = int(input("2 use algorithm to determine best route: "))
    #
    # if val == 0:
    #     packageID = int(input("Type package ID and press enter: "))
    #     selectedPackage = packages.get_package(packageID)
    #     print(selectedPackage.address)
    # elif val == 1:
    #     time = input("Type time (ie 10:55) and press enter: ")
    # elif val == 2:
    #     None
    # else:
    #     print("invalid input, try again")

    # fill distance graph with distances
    distances = Distance()
    distances.get_distances_from_file("WGUPS Distance Table.csv")

    truck1 = truck.Truck("4001 South 700 East", distances)
    truck1.add_package(packages.get_package(2))
    truck1.add_package(packages.get_package(27))
    truck1.view_cargo()
    truck1.deliver()
    packages.print_all_packages_status()
    # truck1.add_package(distances.get_key_from_string("300 State St"))
    #
    # truck1.get_delivery_time(1)
    # truck1.get_delivery_time(2)
