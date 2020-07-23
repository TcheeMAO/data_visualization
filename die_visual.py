import pygal
from die import Die

# Create two six-sided dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D{} and a D{} {} times.".format(die_1.num_sides, die_2.num_sides, len(results))
hist.x_labels = [x for x in range(2, (die_1.num_sides + die_2.num_sides) + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
