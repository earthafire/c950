# Addison Ashworth C950

from excelpackagedataimporter import *
from distancegraph import Distance

# beginning of program
if __name__ == '__main__':

    # packages = get_packages_from_file("WGUPS Package File.csv")
    distances = Distance()
    distances.get_distances_from_file("WGUPS Distance Table.csv")

    distances.get_edges_from_location("380 W 2880 S")