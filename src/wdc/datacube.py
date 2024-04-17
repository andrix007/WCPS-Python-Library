from .connection import DatacubeConnection
from .query import QueryBuilder

#class that represents a datacube and allows to perform operations on it
class Datacube:
    # Connect to the datacube server
    def __init__(self, connection, coverage_id):
        self.connection = connection
        self.coverage_id = coverage_id
        self.operations = []

    # Access a specific datacube and perform a complex query
    def subset(self, lat, lon, time):
        self.operations.append({'type': 'subset', 'params': f"Lat({lat}), Long({lon}), ansi('{time}')"})
        return self

    # Access a specific datacube and perform a complex query
    def range_subset(self, lat, lon, time_range):
        self.operations.append({'type': 'subset', 'params': f"Lat({lat}), Long({lon}), ansi('{time_range}')"})
        return self

    # Fetch the data from the server
    def fetch(self, as_format=None):
        query = QueryBuilder.build(self.coverage_id, self.operations, as_format)
        print("query", query)
        return self.connection.post_query(query)

    # Operations
    def min(self):
        self.operations.append({'type': 'min'})
        return self

    def max(self):
        self.operations.append({'type': 'max'})
        return self

    def avg(self):
        self.operations.append({'type': 'avg'})
        return self

    def count_above(self, threshold):
        self.operations.append({'type': 'count', 'params': f"> {threshold}"})
        return self

    def convert_celsius_to_kelvin(self):
        self.operations.append({'type': 'convert_celsius_to_kelvin'})
        return self

    def on_the_fly_coloring(self, cases):
        self.operations.append({'type': 'on_the_fly_coloring', 'params': cases})
        return self

    def coverage_constructor(self, expression):
        self.operations.append({'type': 'coverage_constructor', 'params': expression})
        return self
