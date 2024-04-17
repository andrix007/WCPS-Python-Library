import unittest
from unittest.mock import MagicMock

#convert the path to the src folder
import sys
sys.path.insert(0, sys.path[0] + '/../src')

from wdc import connect

class TestTemperatureData(unittest.TestCase):
    def setUp(self):
        # Mock the server connection
        self.dbc = connect('https://ows.rasdaman.org/rasdaman/ows')
        self.dbc.post_query = MagicMock()

    def test_fetch_minimum_temperature(self):
        # Setup mock response
        self.dbc.post_query.return_value = b'\"2.2834647\"'
        min_temp_data = self.dbc('AvgLandTemp')
        min_result = min_temp_data.range_subset(53.08, 8.80, "\"2014-01\":\"2014-12\"").min().fetch()
        # Convert byte response to string
        result = min_result.decode('utf-8')
        self.assertEqual(result, "2.2834647")
        print("Minimum Temperature:", result)

    def test_fetch_maximum_temperature(self):
        # Setup mock response
        self.dbc.post_query.return_value = b'\"25.984251\"'
        max_temp_data = self.dbc('AvgLandTemp')
        max_result = max_temp_data.range_subset(53.08, 8.80, "\"2014-01\":\"2014-12\"").max().fetch()
        # Convert byte response to string
        result = max_result.decode('utf-8')
        self.assertEqual(result, "25.984251")
        print("Maximum Temperature:", result)

    def test_calculate_average_temperature(self):
        # Setup mock response
        self.dbc.post_query.return_value = b'\"15.052493472894033\"'
        avg_temp_data = self.dbc('AvgLandTemp')
        avg_result = avg_temp_data.range_subset(53.08, 8.80, "\"2014-01\":\"2014-12\"").avg().fetch()
        # Convert byte response to string
        result = avg_result.decode('utf-8')
        self.assertEqual(result, "15.052493472894033")
        print("Average Temperature:", result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
