# Addison Ashworth C950

from exceldataimporter import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# beginning of program
if __name__ == '__main__':
    print_hi('created by addison')

    packages = get_packages_from_file("WGUPS Package File.csv")
    #print(packages[0])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
