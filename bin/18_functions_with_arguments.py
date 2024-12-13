"""
We are planning to discuss Case-2 here

Case-2: How to pass values to variables present inside the function

3 ways to pass values to variables present inside the function

1-way: WHILE CALLING THE FUNCTION, We can either pass only values OR we can pass values in argument=value
        format
        CALLED AS: POSITIONAL or KEYWORD argument function
2-way: WHILE CALLING THE FUNCTION, We can restrict to pass only values
        CALLED AS: ONLY POSITIONAL argument function
3-way: WHILE CALLING THE FUNCTION, We can restrict to pass values in argument=value
        format
        CALLED AS: KEYWORD argument function
"""

print("""
1-way: WHILE CALLING THE FUNCTION, We can either pass only values OR we can pass values in argument=value
        format
CALLED AS: POSITIONAL or KEYWORD argument function
""")
print("-"*20)
# -----------


def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# WE CAN CALL THIS FUNCTION PASSING ONLY VALUES
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# AND
# WE CAN ALSO CALL THIS FUNCTION PASSING argument_name=Value
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)


print("#"*40, end="\n\n")
#############################

print("""
2-way: WHILE CALLING THE FUNCTION, We can restrict to pass only values
        CALLED AS: ONLY POSITIONAL argument function
""")
print("-"*20)
# -----------

# / -> it is just syntax to tell this function is only-positional argument function
# / -> we are not counting this as argument
# / -> we are not passing any values to this

def employee(name, company, /):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# WE CAN CALL THIS FUNCTION PASSING ONLY VALUES
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# IT WILL NOT WORK
# received_value = employee(name="emp-1", company="comp-1")
# print("received_value:", received_value)


print("#"*40, end="\n\n")
#############################

print("""
3-way: WHILE CALLING THE FUNCTION, We can restrict to pass values in argument=value
        format
        CALLED AS: KEYWORD argument function
""")
print("-"*20)
# -----------

# * -> it is just syntax to tell this function is only-keyword argument function
# * -> we are not counting this as argument
# * -> we are not passing any values to this


def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# THIS WILL NOT WORK
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)

# THIS WILL WORK
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)


print("#"*40, end="\n\n")
#############################
