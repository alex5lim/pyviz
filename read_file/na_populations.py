import pygal

wmap = pygal.maps.world.World()
wmap.title = 'Populations of Countries in North America'
wmap.add('North America', {'ca': 34126000, 'us': 309349000,
                           'mx': 113423000})

wmap.render_to_file('na_populations.svg')
