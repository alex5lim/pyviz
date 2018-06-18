import matplotlib.pyplot as pyplot

x = list(range(1, 5001))
y = [x**3 for x in x]

pyplot.scatter(x, y, s=40, c=y, cmap=pyplot.cm.Blues, edgecolor='none')

# Set chart title and label
pyplot.title("Square Numbers", fontsize=12)
pyplot.xlabel("Value", fontsize=8)
pyplot.ylabel("Square of Value", fontsize=8)

# Set size of tick labels
pyplot.tick_params(axis='both', which='major', labelsize=8)

# Set the range for each axis
pyplot.axis([0, 6000, 0, 135000000000])

# Save the plot to a file named squares_plot.png
pyplot.savefig('squares_plot.png', bbox_inches='tight')
