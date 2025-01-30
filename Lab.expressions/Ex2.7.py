fahrenheit_str = input("Enter the temperature in Fahrenheit: ")

try:
    fahrenheit = float(fahrenheit_str)  # Convert input to float
    celsius = (fahrenheit - 32) * (5/9)  # Calculate Celsius

    print(f"{fahrenheit} °F is equal to {celsius} °C")

except ValueError:
    print("Invalid input. Please enter a valid number for Fahrenheit.")