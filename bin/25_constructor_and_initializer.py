"""
Constructor(__new__) and Initializer(__init__)

When we create object like e1 = Emplpyee()
then both methods will execute
1st __new__ will execute which will create object
then __init__ will execute to initialize object if anything provided

How to rewrite methods which is coming from 'object' class
-> We can rewrite
-> This is called METHOD OVERRIDING
-> concept is called POLYMORPHISM. We can use same method names in current class

In this section,
1) we are planning rewrite/overriding __init__ for passing
    employee name while creating object
2) Declaring class variable directly in class
"""

print("Our Own Class")
print("-"*20)
# -----------


class Employee:

    def __init__(self, ename):
        self.name = ename

    company_name = "XYZ Company"

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def get_employee_name(self):
        return self.name


print("#"*40, end="\n\n")
#############################

print("CLASS and INSTANCE Objects")
print("-"*20)
# -----------

e1 = Employee("emp-1") # __init__(e1, "emp-1")
e2 = Employee("emp-2") # __init__(e2, "emp-2")

print("#"*40, end="\n\n")
#############################

print("DATA present inside each objects:")
print("-"*20)
# -----------

print("DATA present inside class object 'Employee':", Employee.get_company_name())
# object 'Employee' will be passed to 'cls'
print("DATA present inside instance object 'e1':", e1.get_employee_name())
# object 'e1' will be passed to 'self'
print("DATA present inside instance object 'e2':", e2.get_employee_name())
# object 'e2' will be passed to 'self'

print("#"*40, end="\n\n")
#############################

print("METHODS/VARIABLES present inside each objects:")
print("-"*20)
# -----------

print("METHODS/VARIABLES present inside CLASS object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside INSTANCE object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside INSTANCE object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#############################



