class Employee:
    company = "CloudThing"  # This is a class variable

    def __init__(self, name):
        self.name = name    # This is an instance variable

# Creating two employee objects
emp1 = Employee("Ashith")
emp2 = Employee("Ganesh")

# Changing some values
Employee.company = "Kerv Digital"
emp1.company = "My Own Startup"

# What will these two lines print?
print(emp1.company)
print(emp2.company)