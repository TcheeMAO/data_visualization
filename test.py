import matplotlib.pyplot as plt
import sys
import keyboard
from rw_gal import RandomWalkForPygal
import pygal
from die import Die
from random import randint


# Pygal visualization of a random walk
rw = RandomWalkForPygal(4, 20)
rw.fill_walk()

frequencies = []
for value in range(0, rw.max_dist+1):
    frequency = rw.distances.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Result of random walk with a maximum step size of {} and a maximum distance of {} from the origin.".format(rw.max_step, rw.max_dist)
hist.x_labels = [x for x in range(0, rw.max_dist+1)]
hist.x_title = 'Distance from Origin'
hist.y_title = 'Frequency of Distance'

hist.add('Distance', frequencies)
hist.render_to_file('rw_gal.svg')

# Matplotlib visualization of die-rolling
die1 = Die(randint(6, 12))
die2 = Die(randint(6, 12))

