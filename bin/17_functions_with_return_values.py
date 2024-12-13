"""
2 Cases:
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

We are planning to discuss Case-1 here
Case-1: How to access values outside the function
"""

print("Function with 1 return value")
print("-"*20)
# -----------
# 2 steps
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable so that
#       returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return name # Step-1: use 'return' statement inside function to specify values


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#############################

print("Function with more than 1 return values: In Tuple")
print("-"*20)
# -----------
# 2 steps
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable so that
#       returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return (name, company)


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#############################

print("Function with more than 1 return values: In List")
print("-"*20)
# -----------
# 2 steps
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable so that
#       returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#############################

print("Function with more than 1 return values: In Dictionary")
print("-"*20)
# -----------
# 2 steps
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable so that
#       returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#############################
