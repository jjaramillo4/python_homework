import custom_module
import csv
import os
import traceback
from datetime import datetime

employees = {}
minutes1 = ()
minutes2 = ()
minutes_list = []
minutes_set = set()

#Task 2
def read_employees():
    global employees
    employee_list = []
    try:
        with open('../csv/employees.csv','r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                employee_list.append(row)
        employees = {
            "fields": header,
            "rows": employee_list
        } 
        return employees      
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
employees = read_employees()
print(employees)

#Task 3
def column_index(field):
    return employees["fields"].index(field)
employee_id_column = column_index("employee_id")

#Task 4
def first_name(row_number):
    f_name_index =column_index("first_name")
    return employees["rows"][row_number][f_name_index]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches
#Task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task 7
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

#Task 8
def employee_dict(row):
    new_dict =dict(zip(employees['fields'], row))
    new_dict.pop('employee_id')
    return new_dict
#Task 9
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        result[row[0]] = employee_dict(row)
    return result
#Task 10
def get_this_value():
    return os.getenv("THISVALUE")
#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Alakazam")
print(custom_module.secret)

#task 12
def open_csv(csv_path):
    tuple_list = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            tuple_list.append(tuple(row))
    new_dict = {
        "fields":header,
        "rows": tuple_list
    }
    return new_dict

def read_minutes():
   global minutes1
   global minutes2 
   minutes1 = open_csv('../csv/minutes1.csv')
   minutes2 = open_csv('../csv/minutes2.csv')
   print(minutes1)
   print(minutes2)

   return minutes1, minutes2 
read_minutes()

#Task 13
def create_minutes_set():
    global minutes_set
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    minutes_set = set1.union(set2)
    return minutes_set

#Task 14
def create_minutes_list():
    global minutes_list
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set)))
    return minutes_list
    
#Task 15
def write_sorted_list():
    sorted_minute_list = sorted(minutes_list, key=lambda t:t[1])
    final_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minute_list))
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])  # Write header row 
        writer.writerows(final_list)
        return final_list