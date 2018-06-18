from random import choice


class RandomWalk(object):
    """A class to generate random walks."""

    def __init__(self, num_points=50000):
        """"Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x) < self.num_points:
            # Decide which direction to go and how far
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and the next y
            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step

            self.x.append(next_x)
            self.y.append(next_y)
