import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle

import country_codes

filename = "population_data.json"

with open(filename) as file:
    population_data = json.load(file)

    # Build a dictionary of population data.
    cpop_lo, cpop_med, cpop_hi = {}, {}, {}
    for data in population_data:
        if data['Year'] == "2010":
            country_name = data['Country Name']
            population = int(float(data['Value']))
            country_code = country_codes.get_country_code(country_name)
            if country_code:
                if population < 10000000:
                    cpop_lo[country_code] = population
                elif population < 1000000000:
                    cpop_med[country_code] = population
                else:
                    cpop_hi[country_code] = population

print(len(cpop_lo), len(cpop_med), len(cpop_hi))
wmap_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wmap = pygal.maps.world.World(style=wmap_style)
wmap.title = 'World Population in 2010, by Country'
wmap.add('0-10m', cpop_lo)
wmap.add('10m-1bn', cpop_med)
wmap.add('>1bn', cpop_hi)

wmap.render_to_file('world_population.svg')
