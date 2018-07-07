import json

import country_codes

filename = "population_data.json"

with open(filename) as file:
    population_data = json.load(file)

    # Print 2010 population data for each country
    for data in population_data:
        if data['Year'] == "2010":
            population = int(float(data['Value']))
            country_name = data['Country Name']
            country_code = country_codes.get_country_code(country_name)
            if country_code:
                print(country_code + ": " + str(population))
            else:
                print('ERROR-' + country_name)
