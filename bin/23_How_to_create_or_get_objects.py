"""
How to get or create objects
- Using class we can create objects

In this section,
1. CLASS OBJECT
2. INSTANCE OBJECTS
"""

print("Our Own Class")
print("-"*20)
# -----------

class Employee:
    pass

# pass: It is dummy keyword
# pass: use this to keep any block empty
# Above class is valid class even though it is empty
#   that means we can create objects using that class

print("#"*40, end="\n\n")
#############################

print("CLASS and INSTANCE Objects")
print("-"*20)
# -----------

e1 = Employee()
e2 = Employee()

# Total 3 Objects
# CLASS OBJECT: One object with the class name (Employee) will be created automatically
    # What is the use of CLASS OBJECT: To keep data & related methods together
# INSTANCE OBJECTS: e1, e2, which we are creating
    # What is the use of INSTANCE OBJECTS: To keep data & related methods together

print("#"*40, end="\n\n")
#############################

print("Storing Data")
print("-"*20)
# -----------

Employee.company_name = "XYZ Company"
# It will create one variable 'company_name' inside object 'Employee' and store the value

e1.name = "emp-1"
# It will create one variable 'name' inside object 'e1' and store the value

e2.name = "emp-2"
# It will create one variable 'name' inside object 'e2' and store the value

print("#"*40, end="\n\n")
#############################

print("DATA present inside each objects:")
print("-"*20)
# -----------

print("DATA present inside class object 'Employee':", Employee.company_name)
print("DATA present inside instance object 'e1':", e1.name)
print("DATA present inside instance object 'e2':", e2.name)

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

# Question-1: Why data present in class object is visible in all instance objects
# -----------
# They made, class-object is common space for all instance objects
# so, we can make use this common space to keep data which is common for all instance objects
#############################

# Question-2: Why some methods are getting added to all our objects
# -----------
# - there is class called 'object' in builtin
#
# - In this class we have some basic methods written
#   for example: constructing the object method i.e __new__
#       initializind the object method __init__
#
# - by default all classes are linked to 'object' class
#   this linking is called inheritance. So, whatever there
#   in 'object' class will be available in all our classes
#############################

