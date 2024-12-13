"""
Operator Overloading:
In python for each opearator there is name given
Example: __add__ for +

If we want to support + then we need to write __add__ method
in our class

In this section:
1) Support + operator
2) Support Iteration
"""

print("1) Support + operator")
print("-"*20)
# -----------

class Employee:
    def __init__(self, ename):
        self.ename = ename
    def get_name(self):
        return self.ename

    def __add__(self, other): # self=e1, other=e2
        add_result = self.ename + other.ename
        return add_result


e1 = Employee("emp-1")
e2 = Employee("emp-2")

print("Employee 1 Name:", e1.get_name(), end="\n\n")
print("Employee 2 Name:", e2.get_name(), end="\n\n")

# Requirement of +: if we use + b/n e1 & e2 then
# it should concatinare both the names and return

concated_names = e1 + e2 # e1.__add__(e2)
print("concated_names:", concated_names)

print("#"*40, end="\n\n")
#############################

print("2) Support Iteration")
print("-"*20)
# -----------

class Employee:
    def __init__(self, ename):
        self.ename = ename
    def get_name(self):
        return self.ename

    def __add__(self, other): # self=e1, other=e2
        add_result = self.ename + other.ename
        return add_result

    def __iter__(self): # This will be called 1st time & one time only
        self.start_index = 0
        return self

    def __next__(self): # For every iteration, This will be called
        current_index = self.start_index
        if current_index < len(self.ename):
            self.start_index = self.start_index + 1
            return self.ename[current_index]
        else:
            raise StopIteration

e1 = Employee("emp-1")
e2 = Employee("emp-2")

print("Employee 1 Name:", e1.get_name(), end="\n\n")
print("Employee 2 Name:", e2.get_name(), end="\n\n")

# Requirement of +: if we use + b/n e1 & e2 then
# it should concatinare both the names and return

concated_names = e1 + e2 # e1.__add__(e2)
print("concated_names:", concated_names)

print("Iterationg e1:")
for i in e1:
    print("Each Char:", i)

print("\n")

print("Iterationg e2:")
for i in e2:
    print("Each Char:", i)

print("#"*40, end="\n\n")
#############################


