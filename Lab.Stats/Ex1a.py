import matplotlib.pyplot as plt

# Define x and y values
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 1, 8, 7]

# Plot the values as a line graph
plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Simple Line Graph')

# Show the plot
plt.grid(True)
plt.show()
print("What happens now?")
