"""
Inheritance:
1. Multilevel Inheritance
2. Multiple Inheritance
"""

print("1. Multilevel Inheritance")
print("-"*20)
# -----------

# Assume This is existing class
class Salary:
    def add_salary(self, sal):
        self.salary = sal
    def get_salary(self):
        return self.salary

# Add below methods to Salary Class
# 1) add_tax
# 2) get_tax
# 3) modify get_salary method to return (salary-tax)

# Here, we are not modifying existing class Salary,
# Since we have INHERITANCE, we are extending and adding the features

# Salary class: Superclass/parent class
# Employee class: Subclass/childclass
# Whatever there in salary class will come to employee class
class Employee(Salary):
    # 1) add_tax
    def add_tax(self, t):
        self.tax = t

    # 2) get_tax
    def get_tax(self):
        return self.tax

    # 3) modify get_salary method to return (salary-tax)
    # POLYORPHISM: Use same name as super class method name
    # When we call this method, It will override that means super class
    #   method will be hidden
    def get_salary(self):
        return (self.salary - self.tax)

    def get_old_salary_1_way(self):
        old_salary = super().get_salary()
        return old_salary

    def get_old_salary_2_way(self):
        old_salary = Salary.get_salary(self)
        return old_salary

e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.get_salary())
print("Old Salary 1 way:", e1.get_old_salary_1_way())
print("Old Salary 2 way:", e1.get_old_salary_2_way())
print("Tax:", e1.get_tax())

print("#"*40, end="\n\n")
#############################

print("1. Multilevel Inheritance: Method Resolution Order")
print("-"*20)
# -----------

print(Employee.mro())

# If we create object of 'Employee' class and call any methods then
# it will check for method in this order
# [<class '__main__.Employee'>, <class '__main__.Salary'>, <class 'object'>]

print("#"*40, end="\n\n")
#############################

print("2. Multiple Inheritance: Method Resolution Order")
print("-"*20)
# -----------

class A:
    pass
class B:
    pass
class C(A, B):
    pass

print(C.mro())

# If we create object of 'C' class and call any methods then
# it will check for method in this order
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

print("#"*40, end="\n\n")
#############################
