# Inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_detail(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")

class Developer(Employee):
    def role(self):
        print("Developer")

class Manager(Employee):
    def role(self):
        print("Manager")

emp_name = input("Enter employee name: ")
emp_salary = int(input("Enter employee salary: "))
emp1 = Developer(emp_name, emp_salary)
emp2 = Manager(emp_name, emp_salary)
emp1.display_detail()
emp1.role()
emp2.display_detail()
emp2.role()
        