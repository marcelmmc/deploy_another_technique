import pandas as pd
import random

# Read the JSON data into a DataFrame
data = pd.read_json('/Users/marcel/Desktop/finaltry/project-2023-plottwisters/endsong_12.json')

# Set the values of a specific column to be empty
column_name = 'platform'
data[column_name] = ''

new_values_countries = ['BR', 'EC', 'CH', 'IT']  # Replace with your desired values
ips_book = {'BR':'191.242.232.88', 'EC':'190.57.142.118', 'CH':'128.178.3.0', 'IT':'93.47.231.225'} # Replace with your desired values
countries = []
for i in range(len(data)):
    random_number = random.randint(0, len(new_values_countries)-1)
    countries.append(new_values_countries[random_number])

ips = []
for i in countries:
    ips.append(ips_book[i])
# new_values_ip = ['BR':, 'EC':, 'CH':, 'IT':]  # Replace with your desired values

column_name = 'conn_country'
data[column_name] = countries
column_name = 'ip_addr_decrypted'
data[column_name] = ips

# Save the modified DataFrame back to a JSON file
data.to_json('/Users/marcel/Desktop/finaltry/project-2023-plottwisters/anonymised_endsong_12.json', orient='records')