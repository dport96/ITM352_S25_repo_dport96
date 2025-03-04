def generate_numbers(a_student_id, num_reqs):
   # Check that there are at least two requirements available to assign
   if num_reqs < 2:
       raise ValueError("Invalid number of requirements. Must have at  least 2")
   # Remove any dashes or spaces from the student_id
   id = ''.join(filter(str.isdigit, a_student_id))
  
   # Ensure the student_id is valid (8 digits)
   if len(id) != 8:
       raise ValueError("Invalid student ID. It should be 8 digits.")


   # Use a simple algorithm to generate two unique numbers from 1 to num_reqs
   sum_digits = sum(int(digit) for digit in id)
   first_num = (sum_digits % num_reqs) + 1


   product_digits = 1
   for digit in id:
       if int(digit) != 0:  # Avoid multiplying by zero
           product_digits *= int(digit)
   second_num = (product_digits % num_reqs) + 1


   # Ensure the numbers are different
   while second_num == first_num:
       second_num = (second_num % num_reqs) + 1


   return first_num, second_num


# Example usage
try:
   student_id = input("Enter your student id (XXX-XX-XXX): ")
   num1, num2 = generate_numbers(student_id, 10)
   print(f"Your two numbers are: {num1} and {num2}")
except ValueError as e:
   print(f"Error: {e}")
