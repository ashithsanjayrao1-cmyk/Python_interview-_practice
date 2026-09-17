class Developer:
    def get_role(self):
        return "I am a Developer"

class PythonDeveloper(Developer):
    def get_role(self):
        return "I am a Python Developer"

class BackendDeveloper(PythonDeveloper):
    pass

# Creating the objects
dev1 = Developer()
dev2 = BackendDeveloper()

# What will these two lines print?
print(dev1.get_role())
print(dev2.get_role())