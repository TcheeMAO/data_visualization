import matplotlib.pyplot as plt
import sys
import keyboard
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    if keyboard.is_pressed('q'):
        sys.exit()
        break
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.xlabel('X-Values')
    plt.ylabel('Y-Values')

    plt.show()
