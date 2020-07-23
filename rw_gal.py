from random import choice
import math

class RandomWalkForPygal():
    """A class to generate random walks."""

    def __init__(self, max_step, bound=5, num_steps=1000):
        """Initialize attributes of a walk."""
        self.num_steps = num_steps
        self.max_step = max_step
        self.bound = bound
        self.distances = [0]
        self.max_dist = int(round(math.sqrt((bound**2)+(bound**2))))

    def fill_walk(self):
        """Calculate all the points in the walk."""
        current_x = 0
        current_y = 0
        # Keep taking steps until the walk reaches the desired length.
        while len(self.distances) < self.num_steps:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])  # 1 is right, -1 is left
            x_distance = choice([x for x in range(self.max_step+1)])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([y for y in range(self.max_step+1)])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere or leave the boundary.
            if x_step == 0 and y_step == 0:
                continue
            elif abs(current_x+x_step) > self.bound or abs(current_y+y_step) > self.bound:
                continue
            else:
                current_x += x_step
                current_y += y_step
                # Round the distance formula to fit into histograms
                self.distances.append(int(round(math.sqrt((current_x**2)+(current_y**2)))))
