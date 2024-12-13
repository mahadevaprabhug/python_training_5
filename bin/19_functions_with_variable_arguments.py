"""
Functions with variable arguments
1. Functions with POSITIONAL variable arguments
2. Functions with KEYWORD variable arguments
"""

print("1. Functions with POSITIONAL variable arguments")
print("-"*20)
# -----------

def add(*a):
    print("Received Values In Tuple:", a)

add()
add(10)
add(10, 20)
add(10, 20, 30,40)

print("#"*40, end="\n\n")
#############################

print("2. Functions with KEYWORD variable arguments")
print("-"*20)
# -----------


def employee_profile(**a):
    print("Received Values in Dictionary:", a)


employee_profile()
employee_profile(name="emp-1")
employee_profile(name="emp-2", emp_id = 123, phone="12345")

print("#"*40, end="\n\n")
#############################

