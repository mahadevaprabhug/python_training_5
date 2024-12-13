"""
We can combine all type of arguments in one function
BUT we need to follow below order

1st put all positional arguments IF ANY
then
put all positional/keyword arguments IF ANY
then
put variable positional arguments IF ANY
then
put all keyword arguments IF ANY
then
put variable keyword arguments IF ANY
"""

print("1. Functions with 0 arguments")
print("-"*20)
# -----------

def add():
    a = 10
    b = 20
    c = a + b
    print(c)

add()

print("#"*40, end="\n\n")
#############################

print("2. Functions with positional only arguments")
print("-"*20)
# -----------

def add(a, b, /):
    c = a + b
    print(c)

add(10, 20)

print("#"*40, end="\n\n")
#############################

print("3. Functions with keyword only arguments")
print("-"*20)
# -----------

def add(*, a, b):
    c = a + b
    print(c)

add(a=10, b=20)

print("#"*40, end="\n\n")
#############################

print("4. Functions with positional/keyword only arguments")
print("-"*20)
# -----------

def add(a, b):
    c = a + b
    print(c)

add(10, 20)
# OR
add(a=10, b=20)

print("#"*40, end="\n\n")
#############################


print("5. Functions with Few positional and few positional/keyword only arguments")
print("-"*20)
# -----------
# a,b -> Strictly positional
# c,d -> positional/keyword
def add(a, b, /, c, d):
    result = a + b + c + d
    print(result)


add(10, 20, 30, 40)
# OR
add(10, 20, c=30, d=40)
# BELOW CALL WILL NOT WORK
# add(a=10, b=20, c=30, d=40)

print("#"*40, end="\n\n")
#############################

print("6. Functions with Few strictly positional and few keyword only arguments")
print("-"*20)
# -----------
# a,b -> Strictly positional
# c,d -> Strictly keyword
def add(a, b, *, c, d):
    result = a + b + c + d
    print(result)

# BELOW CALL WILL NOT WORK
# add(10, 20, 30, 40)
# OR
add(10, 20, c=30, d=40)
# BELOW CALL WILL NOT WORK
# add(a=10, b=20, c=30, d=40)

print("#"*40, end="\n\n")
#############################

print("6. Functions with variable positional and variable keyword ")
print("-"*20)
# -----------


def add(*a, **b):
    print("Receive Variable positional arguments:", a)
    print("Receive Variable keyword arguments:", b)

add()
add(10, 20, 30)
add(x=10, y=20)
add(10, 20, 30, x=10, y=20, z=30)

print("#"*40, end="\n\n")
#############################
