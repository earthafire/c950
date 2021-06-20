class PackageHashTable:

    # big O: O(1)
    def __init__(self):
        self.current_size = 25
        self.filled_slots = 0
        self.data = [None] * self.current_size  # list of packages

    def get_filled_slots(self):
        return self.filled_slots

    def get_hash(self, value):
        return value % self.current_size

    def is_full(self):  # check if array is close to full
        if self.filled_slots > self.current_size - 10:
            return True
        else:
            return False

    def double_table_capacity(self):  # double size of current array
        for x in range(0, self.current_size):
            self.data.append(None)
        self.current_size *= 2

    # big O: O(1)
    def add_package(self, new_package):
        package_num = self.get_hash(new_package.package_id)

        if self.data[package_num] is None:
            self.filled_slots += 1  # keeps track of how many full slots in order to prevent filling it up

        self.data[package_num] = new_package  # set index to new package

        if self.is_full():  # if the hashtable is getting full, add another 40 slots
            self.double_table_capacity()

    # big O(1) time to retrieve package
    def get_package(self, int_id):
        package = self.data[self.get_hash(int_id)]
        if package is None:
            print("No such package found!")
        return package

    # big O(1) time to edit package
    def edit_package_status(self, int_key, status):
        package_to_edit = self.get_package(int_key)
        if package_to_edit is None:
            print("No such package found!")
        else:
            package_to_edit.status = status

    def print_all_packages_status(self):
        for item in self.data:
            if item is not None:
                item.print()
