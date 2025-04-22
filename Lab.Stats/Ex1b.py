import matplotlib.pyplot as plt

# Define x and y values
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 1, 8, 7]

# First figure: Line Plot
plt.figure("Line Plot")
plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Line Plot')
plt.grid(True)

# Second figure: Scatter Plot
plt.figure("Scatter Plot")
plt.scatter(x_values, y_values, color='red', marker='o')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot')
plt.grid(True)

# Show both plots
plt.show()
