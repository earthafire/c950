import datetime
import distancegraph


class Truck:
    def __init__(self, current_address, start_time, distance_map: distancegraph):
        self.location = current_address
        self.packages = []
        self.start_time = start_time  # when the truck leaves the hub to deliver the first package
        self.speed = 18  # miles per hour
        self.distance_map = distance_map

    def set_start_time(self, new_time):
        self.start_time = new_time

    def add_package(self, new_package):
        self.packages.append(new_package)

    def deliver_to_time(self, stop_time):
        distance = 0
        end_time = datetime.datetime(1, 1, 1, self.start_time.hour, self.start_time.minute, self.start_time.second)

        if end_time < stop_time:
            # leave hub and change package status
            for item in self.packages:
                item.status = "en route"

            # start all packages
            for item in self.packages:
                # calculate next move
                next_distance = self.distance_map.get_distance_from_location_to_locations(self.location, item.address)
                seconds_to_destination = next_distance / self.speed * 60 * 60

                # move truck if time is not already up
                end_time = end_time + datetime.timedelta(seconds=seconds_to_destination)
                if end_time <= stop_time:
                    self.location = item.address
                    distance += next_distance
                    item.status = "delivered {0}:{1:0>2}".format(end_time.hour, end_time.minute)
                    # print("Traveled {0} miles to deliver packageID {1} at {2}:{3:0>2}"
                    #       .format(next_distance, item.package_id, end_time.hour, end_time.minute))
                else:
                    end_time = stop_time
                    break

        print("Distance traveled: {0:.2f} miles - End time: {1}:{2:0>2}"
              .format(distance, end_time.hour, end_time.minute))

        data = [end_time, distance]
        return data

    def view_cargo(self):
        for item in self.packages:
            item.print()
