import pygal
from datetime import datetime

from die import Die


# Create a D6 die
die = Die()

# Roll the die and save the results
results = []
for roll_num in range(1000):
    results.append(die.roll())

# Count the freqency of each result
frequency = []
for value in range(1, die.num_sides+1):
    frequency.append(results.count(value))

# Create dice roll histogram
histogram = pygal.Bar()
histogram.title = "Results of rolling dice 1000 times"
histogram.x_labels = ['1', '2', '3', '4', '5', '6']
histogram.x_title = "Result"
histogram.y_label = "Frequency of result"
histogram.add('D6', frequency)

# Generate filename
filename = 'dice_roll_histogram_'
filename += datetime.now().strftime('%Y%m%d-%H%M%S')
filename += '.svg'

# Render histogram and save it to a file
print('Render results to ' + filename)
histogram.render_to_file(filename)
