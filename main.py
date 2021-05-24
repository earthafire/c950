# Addison Ashworth C950

from excelpackagedataimporter import *
from distancegraph import Distance

# beginning of program
if __name__ == '__main__':

    # TODO:load packages into hash map
    # TODO:load packages into trucks

    print("Make a selection")
    print("0 look up package id")
    print("1 look up packages at time")
    val = input("2 use algorithm to determine best route: ")

    if val == 0:
        packageID = input("Type package ID and press enter: ")
    elif val == 1:
        time = input("Type time (ie 10:55) and press enter: ")
    elif val == 2:
        None
    else:
        print("invalid input, try again")

    # packages = get_packages_from_file("WGUPS Package File.csv")
    distances = Distance()
    distances.get_distances_from_file("WGUPS Distance Table.csv")

    distances.get_distance_from_location_to_locations("380 W 2880 S", "300 State St")
