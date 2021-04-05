import csv
from package import Package


def get_packages_from_file(filename):
    packagelist = []
    file = open(filename, 'r')
    reader = csv.DictReader(file)

    for row in reader:
        print(row.items())
        packagelist.append(Package(row["Package\nID"], row["Address"], row["City "], row["State"], row["Zip"], row["Delivery\nDeadline"], row["Mass\nKILO"]))
