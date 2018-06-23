import pygal
from datetime import datetime


from die import Die


# Create two D6 dice
d1 = Die(int(input("First dice size = ")))
d2 = Die(int(input("Second dice size = ")))

# Roll the dice and save the results
d1_results = []
d2_results = []
combined_results = []
for value in range(1000):
    d1_result = d1.roll()
    d2_result = d2.roll()
    d1_results.append(d1_result)
    d2_results.append(d2_result)
    combined_results.append(d1_result + d2_result)

# Count frequency of the results
d1_frequency = []
d2_frequency = []
combined_frequency = []

for num in range(1, d1.num_sides + 1):
    d1_frequency.append(d1_results.count(num))

for num in range(1, d2.num_sides + 1):
    d2_frequency.append(d2_results.count(num))

for num in range(2, d1.num_sides + d2.num_sides + 1):
    combined_frequency.append(combined_results.count(num))

# Normalized frequency
for num in range(d1.num_sides, d1.num_sides + d2.num_sides):
    d1_frequency.append(None)

for num in range(d2.num_sides, d1.num_sides + d2.num_sides):
    d2_frequency.append(None)

combined_frequency.insert(0, None)

# Create histogram
histogram = pygal.Bar()
histogram.title = "Results of rolling dice 1000 times"
histogram.x_labels = map(str, range(1, d1.num_sides + d2.num_sides + 1))
histogram.x_title = "Result"
histogram.y_title = "Frequency of result"
histogram.add("Dice-1(size={0})".format(d1.num_sides), d1_frequency)
histogram.add("Dice-2(size={0})".format(d2.num_sides), d2_frequency)
histogram.add("Combined", combined_frequency)

# Create filename
filename = "dice_roll_result_"
filename += datetime.now().strftime('%Y%m%d-%H%M%S')
filename += ".svg"

# Render histogram to file
print("Render result to " + filename)
histogram.render_to_file(filename)
