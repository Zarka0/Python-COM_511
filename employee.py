#Write a program to implement an employee management system using classes, instances and 
#inheritance.
class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")

class Manager(Employee):
    def __init__(self, employee_id, name, salary, department):
        super().__init__(employee_id, name, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

# Example usage:

# Create regular employee
employee1 = Employee(1, "John Doe", 50000)
employee1.display_details()

print("\n")

# Create manager
manager1 = Manager(2, "Jane Smith", 70000, "IT")
manager1.display_details()