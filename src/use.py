from wdc import connect

# Connect to the datacube server
dbc = connect('https://ows.rasdaman.org/rasdaman/ows')

# Fetch the minimum temperature value
min_temp_data = dbc('AvgLandTemp')
min_result = min_temp_data.range_subset(53.08, 8.80, "\"2014-01\":\"2014-12\"").min().fetch()
print("Minimum Temperature:", min_result.decode('utf-8'))

# Fetch the maximum temperature value
max_temp_data = dbc('AvgLandTemp')
max_result = max_temp_data.range_subset(53.08, 8.80, "\"2014-01\":\"2014-12\"").max().fetch()
print("Maximum Temperature:", max_result.decode('utf-8'))

# Calculate average temperature
avg_temp_data = dbc('AvgLandTemp')
avg_result = avg_temp_data.range_subset(53.08, 8.80, "\"2014-01\":\"2014-12\"").avg().fetch()
print("Average Temperature:", avg_result.decode('utf-8'))
