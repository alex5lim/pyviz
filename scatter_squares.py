import matplotlib.pyplot as pyplot

x = list(range(1, 1001))
y = [x**2 for x in x]

pyplot.scatter(x, y, s=10)

# Set chart title and label
pyplot.title("Square Numbers", fontsize=12)
pyplot.xlabel("Value", fontsize=8)
pyplot.ylabel("Square of Value", fontsize=8)

# Set size of tick labels
pyplot.tick_params(axis='both', which='major', labelsize=8)

# Set the range for each axis
# pyplot.axis([0, 1100, 0, 1100000])

pyplot.show()
