import matplotlib.pyplot as plt
import numpy as np

max_x = 10000
min_x = -300
x_values, y_values = [], []

file = open('dataPoints.txt', 'r')

for line in file:
        row = line.split()
        x_values.append(int(row[0]))
        y_values.append(int(row[1]))

plt.title('Title')
plt.xlabel('Evaluation')
plt.ylabel('Fitness Score')
plt.xlim([min_x, max_x])
plt.scatter(x_values, y_values)
plt.show()
