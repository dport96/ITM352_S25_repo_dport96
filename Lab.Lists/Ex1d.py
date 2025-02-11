first_name = input('first name: ')
middle_initial = input('middle initial: ')
last_name = input('last name: ')
a_string = "{} {} {}"
full_name = a_string.format(first_name, middle_initial, last_name)

print(full_name)