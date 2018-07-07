import json

filename = "population_data.json"

with open(filename) as file:
    population_data = json.load(file)

    # Print 2010 population data for each country
    for data in population_data:
        if data['Year'] == "2010":
            print(data['Country Name'] + ": " + data['Value'])
