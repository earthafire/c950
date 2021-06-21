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
    truck1 = truck.Truck("4001 South 700 East", datetime.datetime(1, 1, 1, hour=8), distances)
    truck2 = truck.Truck("4001 South 700 East", datetime.datetime(1, 1, 1, hour=8), distances)
    truck3 = truck.Truck("4001 South 700 East", datetime.datetime(1, 1, 1, hour=8), distances)

    # ask for user input
    print("Make a selection")
    print("0 Look up package by ID")
    print("1 Look up the status of all packages at a specific time")
    print("2 Use algorithm to determine best route")
    val = int(input("Int input: "))

    packages_left = []
    greedy_algorithm = algorithm.NearestNeighbor(distances)

    for x in range(1, packages.get_filled_slots() + 1):
        if x == 9:
            packages.get_package(x).address = "410 S State St"

        packages_left.append(packages.get_package(x))

    if val == 0:
        # retrieve package data from hashtable in big O(1) time
        packageID = int(input("Type package ID and press enter: "))
        selectedPackage = packages.get_package(packageID)
        # show package data
        selectedPackage.print()
    elif val == 1:
        # load packages into trucks using previous data from algorithm
        algorithm.load_trucks(truck1, truck2, truck3, packages)

        # simulate trucks driving routes until selected time
        time = datetime.datetime.fromisoformat("0001-01-01T" + input("Type time (HH:MM) and press enter: ") + ":00")

        mileage = 0

        data1 = truck1.deliver_to_time(time)
        data2 = truck2.deliver_to_time(time)

        # truckload 3 is filled when truckload 1 or 2 arrives
        if data1[0] < data2[0]:
            truck3.set_start_time(data1[0])
        else:
            truck3.set_start_time(data2[0])

        # truck3 delivers after any truck arrives
        data3 = truck3.deliver_to_time(time)
        mileage = data1[1] + data2[1] + data3[1]
        print("total mileage: {0:.2f} miles".format(mileage))
        print()
        # show all package status at end of simulation
        packages.print_all_packages_status()

    elif val == 2:
        greedy_algorithm.greedy_sort(packages_left)
    else:
        print("invalid input, try again")
