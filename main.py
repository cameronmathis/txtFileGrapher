import matplotlib.pyplot as plt

# Name of .txt file containing data points
txt_file = "dataPoints.txt"

# Set table title
table_title = "Title"

# Set both X & Y Label
x_label = "X-Label"
y_label = "Y_Label"

# Set range for both X & Y Axis
min_x = -300
max_x = 10000
min_y = -300
max_y = 10000

# Initialize array for both X & Y Values
x_values, y_values = [], []

# Open .txt file
file = open(txt_file, 'r')

# Read in data from .txt file
for line in file:
        row = line.split()
        x_values.append(int(row[0]))
        y_values.append(int(row[1]))

# Create scatter plot
plt.title(table_title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.xlim([min_x, max_x])
plt.ylim([min_x, max_x])
plt.scatter(x_values, y_values)
plt.show()
