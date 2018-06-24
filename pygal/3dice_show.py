import pygal
from datetime import datetime

from die import Die


# Create dice
d1 = Die()
d2 = Die()
d3 = Die()

# Roll the dice
result = []

for i in range(1000):
    result.append(d1.roll() + d2.roll() + d3.roll())

# Count frequency
frequency = []
for num in range(3, d1.num_sides + d2.num_sides + d3.num_sides + 1):
    frequency.append(result.count(num))

# Create histogram
histogram = pygal.Bar()
histogram.title = "Result of 3 D6 dice roll"
histogram.x_labels = map(str, range(3, d1.num_sides + d2.num_sides + d3.num_sides + 1))
histogram.x_title = "Result"
histogram.y_title = "Frequency"
histogram.add("3 D6 dice", frequency)

# Render to a file
filename = "dice_roll_result_"
filename += datetime.now().strftime("%Y%m%d-%H%M%S")
filename += ".svg"
print("Render the result to {0}".format(filename))
histogram.render_to_file(filename)
