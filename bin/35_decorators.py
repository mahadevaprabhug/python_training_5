"""
Decorators:
"""

print("WITHOUT Using Decorator")
print("-"*20)
# -----------


def add(a, b):
    print("Result is:")
    print(a+b)
    print("End of the result", end="\n\n")


def sub(a, b):
    print("Result is:")
    print(a-b)
    print("End of the result", end="\n\n")


add(10, 20)
sub(10, 20)

print("#"*40, end="\n\n")
#############################

print("Using Decorator: PARTIAL IMPLEMENTATION")
print("-"*20)
# -----------


# As per decorator design pattern
def my_decorator(my_func): # my_func=add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        my_func(x,y) # sub(10,20)
        print("End of the result", end="\n\n")
    return decorated_function


def add(a, b):
    print(a+b)

def sub(a, b):
    print(a-b)


received_function = my_decorator(add)
# received_function will be having n decorated_function reference
received_function(10, 20)

received_function = my_decorator(sub)
# received_function will be having n decorated_function reference
received_function(10, 20)

print("#"*40, end="\n\n")
#############################

print("Using Decorator: FINAL IMPLEMENTATION")
print("-"*20)
# -----------


# As per decorator design pattern
def my_decorator(my_func): # my_func=add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        my_func(x,y) # sub(10,20)
        print("End of the result", end="\n\n")
    return decorated_function


@my_decorator
def add(a, b):
    print(a+b)


@my_decorator
def sub(a, b):
    print(a-b)


add(10, 20)
sub(10, 20)

# @my_decorator will take care of below 2 steps
# received_function = my_decorator(add)
# received_function(10, 20)

# @my_decorator will take care of below 2 steps
# received_function = my_decorator(sub)
# received_function(10, 20)

print("#"*40, end="\n\n")
#############################
