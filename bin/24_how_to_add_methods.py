"""
How to add methods

In this section,
1. CLASS METHODS:
2. INSTANCE METHODS:
3. STATIC METHODS

Features Supported:
1. storing company name method
2. storing employee name method
3. getting company name method
4. getting employee name method
5. employee name startswith method
"""

print("Our Own Class")
print("-"*20)
# -----------


class Employee:
    """
    Features Supported:
    1. storing company name method
    2. storing employee name method
    3. getting company name method
    4. getting employee name method
    5. employee name startswith method
    6. get_average_salary method
    """

    # 1. storing company name method
    @classmethod
    def store_company_name(cls, cname):
        cls.company_name = cname

    # 3. getting company name method
    @classmethod
    def get_company_name(cls):
        return cls.company_name

    # 2. storing employee name method
    def store_employee_name(self, ename):
        self.name = ename

    # 4. getting employee name method
    def get_employee_name(self):
        return self.name

    # 5. employee name startswith method
    def employee_name_startswith(self, prefix):
        result = self.name.startswith(prefix)
        return result

    # 6. get_average_salary method
    # If we pass 2 numbers, it should return average
    # So, inside method no need of INSTANCE or CLASS objects
    @staticmethod
    def get_average_salary(sal1, sal2):
        return (sal1+sal2)/2

print("#"*40, end="\n\n")
#############################

print("CLASS and INSTANCE Objects")
print("-"*20)
# -----------

e1 = Employee()
e2 = Employee()

print("#"*40, end="\n\n")
#############################

print("Storing Data")
print("-"*20)
# -----------

Employee.store_company_name("XYZ Company")
# Internally object 'Employee' will goto 'cls' and "XYZ Company" will be passed to 'cname'

e1.store_employee_name("emp-1")
# Internally object 'e1' will goto 'self' and "emp-1" will be passed to 'ename'
# OR
# Employee.store_employee_name(e1, "emp-1")

e2.store_employee_name("emp-2")
# Internally object 'e2' will goto 'self' and "emp-2" will be passed to 'ename'
# OR
# Employee.store_employee_name(e2, "emp-2")


# About @classmethod
# - This is called decorator
# - This is also function
# - In this decorator, they wrote a logic to pass CLASS object
#   to below defined method. It wll always be on top of method

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

avg_salary = Employee.get_average_salary(2000, 4000)
print("avg_salary:", avg_salary)

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

print("Employee-1 name startswith 'emp'?:", e1.employee_name_startswith("emp"))
