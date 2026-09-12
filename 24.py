class Employee:
    company_name = "Tech Startup"


    def __init__(self,name):
        self.name = name


emp1 = Employee("Alice")

emp2 = Employee("Bob")

emp1.company_name = "Global Tech"

print(emp1.company_name)
print(emp2.company_name)