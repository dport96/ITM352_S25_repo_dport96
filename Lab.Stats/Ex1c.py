import matplotlib.pyplot as plt

# Define x and y values
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 1, 8, 7]

# figure: Scatter Plot
plt.figure("Scatter Plot")
plt.scatter(x_values, y_values, color='red', marker='o')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot')
plt.grid(True)

x2_values = [1.5, 2.5, 3.1, 4.1, 5.4]
y2_values = [4,1,1,5,5]
plt.plot(x2_values, y2_values, marker='o', linestyle='-', color='blue')


# Show both plots
plt.show()
