# This is to explore different basic functions in python!!!

print('What is your name')  # Get full name
emp_Name = input('>')

print('What is your current salary')
salary = float(input('>'))
rounded_salary = round(salary)
salary_hike = float(salary) * 0.30
new_salary = salary + float(salary_hike)
new_salary_annum = str(int(new_salary)) + ' per annum'

print(f'Salary in float is Rs.{salary}')
print(f'Salary round to Rs.{rounded_salary}')
print(f'Your new salary will be Rs.{new_salary}')
print(f'New salary per annum will be Rs.{new_salary_annum}')
print(f'The length of the name is: {len(emp_Name)}')