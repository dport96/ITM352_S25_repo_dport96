import csv

csv_filename = 'my_custom_spreadsheet.csv'

salaries = []

# read the CSV salaary spreadsheet and get the salaraies as a list
with open(csv_filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip the header row
    print(headers)
    salary_index = headers.index("Annual_Salary")  # Find the correct column index

    for row_data in reader:
        salaries.append(float(row_data[salary_index]))

# compute salaray statistics
avg_salary = sum(salaries) / len(salaries) if salaries else 0
max_salary = max(salaries) if salaries else 0
min_salary = min(salaries) if salaries else 0

print(f"Average Salary: ${avg_salary:,.2f}")
print(f"Maximum Salary: ${max_salary:,.2f}")
print(f"Minimum Salary: ${min_salary:,.2f}")