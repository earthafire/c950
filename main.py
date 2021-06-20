# Name: Addison Ashworth - Student ID: 001393715
import datetime

import algorithm
import truck
import excelpackagedataimporter
from distancegraph import Distance

# beginning of program
if __name__ == '__main__':
    # fill custom hashtable with package data from csv file
    packages = excelpackagedataimporter.get_packages_from_file("WGUPS Package File.csv")

    # fill distance graph with values from csv file
    distances = Distance()
    distances.get_distances_from_file("WGUPS Distance Table.csv")

    # initialize trucks
    truck1 = truck.Truck("4001 South 700 East", datetime.datetime(1, 1, 1, hour=7), distances)
    truck2 = truck.Truck("4001 South 700 East", datetime.datetime(1, 1, 1, hour=7), distances)

    # ask for user input
    print("Make a selection")
    print("0 look up package id")
    print("1 look up status of all packages at specific time")
    val = int(input("2 use algorithm to determine best route: "))

    if val == 0:
        # retrieve package data from hashtable in big O(1) time
        packageID = int(input("Type package ID and press enter: "))
        selectedPackage = packages.get_package(packageID)
        # show package data
        selectedPackage.print()
    elif val == 1:
        # load packages into trucks using previous data from algorithm
        algorithm.load_trucks(truck1, truck2, packages)

        # simulate trucks driving routes until selected time
        time = datetime.datetime.fromisoformat("0001-01-01T" + input("Type time (HH:MM) and press enter: ") + ":00")

        truck1.deliver_to_time(time)
        truck2.deliver_to_time(time)
        print()
        # show all package status at end of simulation
        packages.print_all_packages_status()
    elif val == 2:
        None
    else:
        print("invalid input, try again")


def load_trucks(self):
    None
