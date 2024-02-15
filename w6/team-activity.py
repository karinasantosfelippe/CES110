"""
Author: Karina Santos Felippe
Activity:
    Consider the scenario of a Human Resources (HR) system. It contains various information about the employees of a company, such as their names, ID numbers, job titles, salaries, etc. From this data you may need to run a payroll process to generate paychecks, generate information for tax purposes, or produce any number of reports of various kinds.
Core Requirements:
    1. Download the file and save it to your computer. In VS Code, open the folder that contains this file. Then, create a new Python script in that folder.
    2. Have your program open the HR System file, read through it line by line, and at this point, simply display the line to the screen.
    3. Split the line into parts and change your display, so that it shows only the names (instead of the whole line).
    4. For each line, get the name and the job title for each person, and display those to the screen.
Stretch challenge:
    1. Strip off any leading and trailing whitespace from each line.
        In addition to the name and the job title, also access the salary and the ID number and save them into variables. Display all four values in this format: name (ID: id_number), job_title - $salary. Don't forget to convert the salary to a number and display it with two decimals.
    2. Instead of displaying the salary information, calculate and display a paycheck amount for the employee. Assume that they are paid twice a month.
    3. Change the program so that it generates bonuses for anyone who is an engineer. For each of these employees, add $1000 to their paycheck amount.
"""

'''
## CORE REQUIREMENTS
employee_info = ""
with open("hr_system.txt") as hr_data:
    for employee in hr_data:
        employee_info = employee.split()
        print(f"Name: {employee_info[0]}, Title: {employee_info[2]}")
'''

## STRECH CHALLENGE

employee_info = ""
with open("sources/hr_system.txt") as hr_data:
    for employee in hr_data:
        employee_info = employee.strip().split(" ")

        name = employee_info[0]
        id_number = employee_info[1]
        job_title = employee_info[2]
        salary = float(employee_info[3])
        pay_amount = salary / 24

        if job_title.lower() == 'engineer':
            pay_amount += 1000

        print(f"{name} (ID: {id_number}), {job_title} - ${pay_amount:.2f}")