import matplotlib.pyplot as pyplot

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of plotting window
    pyplot.figure(dpi=128, figsize=(10, 6))

    # Plot the points
    point_numbers = list(range(rw.num_points))
    pyplot.scatter(rw.x, rw.y, c=point_numbers, cmap=pyplot.cm.Blues,
                   edgecolor='none', s=1)

    # Plotting the first and last points.
    pyplot.scatter(0, 0, c='green', edgecolor='none', s=20)
    pyplot.scatter(rw.x[-1], rw.y[-1], c='red', edgecolor='none', s=20)

    # Cleaning up the Axes
    pyplot.axes().get_xaxis().set_visible(False)
    pyplot.axes().get_yaxis().set_visible(False)

    # Show the plot
    pyplot.show()

    if input("Make another walk? (y/n) ").lower() == 'n':
        break
