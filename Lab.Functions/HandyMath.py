def midpoint(begin_point, end_point):
    mdpt = (begin_point + end_point)/2
    return mdpt

def squareroot(number):
    return number**0.5

def exponent(base, exponent):
  """
  Calculates the value of a base raised to an exponent.

  Args:
    base: The base number.
    exponent: The exponent to raise the base to.

  Returns:
    The value of base raised to the power of exponent.
  """
  return base**exponent

def max(num1, num2):
   return (num1 > num2)*num1 + (num1 <= num2)*num2

def min(num1, num2):
  """
  Returns the smaller of two numbers using a conditional expression.

  Args:
    num1: The first number.
    num2: The second number.

  Returns:
    The smaller of the two numbers.
  """
  return num1 if num1 <= num2 else num2  # Conditional expression (ternary operator)

print("HandyMath loaded...")