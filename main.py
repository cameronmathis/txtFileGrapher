import matplotlib.pyplot as plt

x_values, y_values = [], []

file = open('dataPoints.txt', 'r')

for line in file:
        row = line.split()
        x_values.append(int(row[0]))
        y_values.append(int(row[1]))

plt.title('Title')
plt.xlabel('Evaluation')
plt.ylabel('Fitness Score')
plt.scatter(x_values, y_values)
plt.show()
