import csv
from package import Package
from packagehashtable import PackageHashTable


class Location:
    def __init__(self, address):
        self.address = address


class Graph:
    def __init__(self):
        self.verticesList = {}
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_location, csv_index):
        self.adjacency_list[new_location] = []
        self.verticesList[csv_index] = [new_location]

    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


class Distance:
    def __init__(self):
        self.values = Graph()

    # resets values to file default
    def get_distances_from_file(self, filename):
        """takes a csv filename and fills in internal Graph with values from file"""
        # wipe old graph
        self.values = Graph()

        # open csv file
        file = open(filename, newline='')
        reader = csv.reader(file, delimiter=',')
        row_number = -1

        # read csv row by row
        for row in reader:
            row_number += 1
            if row_number == 0:
                # the first row creates all the vertices
                csv_column_index = -1
                for item in row:
                    csv_column_index += 1
                    if len(item) > 1 and not item.__contains__("DISTANCE"):
                        self.values.add_vertex(item, csv_column_index)
            else:
                # the next rows contain data on weighted edges
                from_vertex = None
                csv_column_index = -1
                for item in row:
                    csv_column_index += 1  # keeps track of the column
                    if csv_column_index == 0:
                        # the first column is the name of the vertex
                        from_vertex = item

                    elif csv_column_index == 1:
                        # we skip the second column, its the address only
                        continue

                    else:
                        item = float(item)

                        if item == 0:
                            # we are done with this row if we find a 0
                            break

                        # the rest of the items are weights for each edge attached to this vertex
                        to_vertex = self.values.verticesList.get(csv_column_index)[0]
                        # print("make undirected edge from: ", from_vertex, " and to: ", to_vertex, " with weight: ", item)
                        self.values.add_undirected_edge(from_vertex, to_vertex, item)

    def get_key_from_string(self, string):
        """return first key containing string"""
        for item in self.values.adjacency_list.keys():
            if item.__contains__(string):
                # print("I found: " + item)
                return item

    def get_distance_from_location_to_locations(self, start_location, end_location):
        """takes a location or list of locations and returns all edges leading away from it"""

        start_loc_key = self.get_key_from_string(start_location)
        end_loc_key = self.get_key_from_string(end_location)

        if end_loc_key is None or start_loc_key is None:
            return None

        answer = self.values.edge_weights[start_loc_key, end_loc_key]
        print("distance to " + end_loc_key + " is ")

        print(answer)

        return self.values.edge_weights[start_loc_key, end_loc_key]
