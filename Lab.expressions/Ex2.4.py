user_input = input("Please enter a decimal number between 1 and 100: ")
# convert input to a number and compute its square
number = float(user_input)
squared_number = number ** 2

print(f"You entered the number: {number}")
print(f"The square of {number} is: {round(squared_number, 2)}")