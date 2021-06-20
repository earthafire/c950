import packagehashtable
import truck


def load_trucks(truck1: truck, truck2: truck, packages):
    for x in range(1, 21):
        truck1.add_package(packages.get_package(x))
    for x in range(21, 41):
        truck2.add_package(packages.get_package(x))