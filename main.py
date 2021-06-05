# Addison Ashworth C950
import excelpackagedataimporter
import truck
from excelpackagedataimporter import *
from distancegraph import Distance

# beginning of program
if __name__ == '__main__':

    packages = get_packages_from_file("WGUPS Package File.csv")
    # TODO:load packages into trucks

    print("Make a selection")
    print("0 look up package id")
    print("1 look up packages at time")
    val = int(input("2 use algorithm to determine best route: "))

    if val == 0:
        packageID = int(input("Type package ID and press enter: "))
        selectedPackage = packages.get_package(packageID)
        print(selectedPackage.address)
    elif val == 1:
        time = input("Type time (ie 10:55) and press enter: ")
    elif val == 2:
        None
    else:
        print("invalid input, try again")

    # distances = Distance()
    # distances.get_distances_from_file("WGUPS Distance Table.csv")
    #
    # distances.get_distance_from_location_to_locations("380 W 2880 S", "300 State St")

    # truck1 = truck.Truck
    # truck1.add_package(distances.get_key_from_string("380 W 2880 S"))
    # truck1.add_package(distances.get_key_from_string("300 State St"))
    #
    # truck1.get_delivery_time(1)
    # truck1.get_delivery_time(2)
