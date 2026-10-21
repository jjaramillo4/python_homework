#Task 3
import csv

with open('../csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    rows = list(reader)  

    employee_names = [row[1] + " "+ row[2] for row in rows]
    print(employee_names)

    names_with_e = [name for name in employee_names if 'e' in name.lower()]
    print(names_with_e)