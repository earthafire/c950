import package


class HashItem:
    def __init__(self, key, parcel):
        self.key = key
        self.package = parcel


class PackageHashTable:

    # big O: O(1)
    def __init__(self):
        self.current_size = 25
        self.filled_slots = 0
        self.data = [] * self.current_size  # list of packages

    # big O: O(1)
    def add_package(self, new_package):
        new_hash_item = HashItem(new_package.package_id, new_package)
        packagenum = new_hash_item.key % self.current_size
        self.data.insert(packagenum, new_hash_item)  # hash is current size
        self.filled_slots += 1  # keeps track of how many full slots in order to prevent filling it up

        if self.filled_slots / self.current_size > .9:  # if the hashtable is getting full, add another 40 slots
            # print("increasing size of hashtable")
            self.current_size = self.current_size + 25
            for x in range(0, 24):
                self.data.append(None)

    # big O(1) time to retrieve package
    def get_package(self, int_id):
        return self.data[int_id]

    # big O(1) time to edit package
    def edit_package_status(self, int_key, status):
        package_to_edit = self.get_package(int_key)
        if package_to_edit is None:
            print("No such package found!")
        else:
            package_to_edit.status = status
