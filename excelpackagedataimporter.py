import csv
from package import Package
from packagehashtable import PackageHashTable


def get_packages_from_file(filename):
    package_hash = PackageHashTable()
    file = open(filename, 'r')
    reader = csv.DictReader(file)

    # each row represents a package (first row is header)
    for row in reader:
        package_hash.add_package(Package(int(row["Package\nID"]), row["Address"], row["City "], row["State"], row["Zip"], row["Delivery\nDeadline"], row["Mass\nKILO"]))

    return package_hash
