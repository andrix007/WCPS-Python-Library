from .connection import DatacubeConnection
from .datacube import Datacube

def connect(server_url):
    connection = DatacubeConnection(server_url)
    return lambda coverage_id: Datacube(connection, coverage_id)
