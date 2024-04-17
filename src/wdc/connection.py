import requests
import logging

# class that represents a connection to a datacube server
class DatacubeConnection:
    def __init__(self, server_url):
        self.server_url = server_url

        # Enable debug logging
        logging.basicConfig(level=logging.DEBUG)

    def post_query(self, query):

        # Send the WCPS query to the server
        logging.debug(f"Sending WCPS query: {query}")
        response = requests.post(f"{self.server_url}/wcps", data={'query': query}, verify=False)

        # Check if the query was successful
        if response.status_code == 200:
            return response.content
        else:
            logging.error(f"Failed to execute query with status {response.status_code}: {response.text}")
            raise Exception(f"Failed to execute query: {response.text}")
