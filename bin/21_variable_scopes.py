"""
Variable Scopes
1. Local Scope
2. Enclosed Scope
3. Global Scope
4. Builtin Scope
"""

print("1. Local Scope")
print("-"*20)
# -----------

def add():
    a = 10 # In Local Scope: We can access within the function only

print("#"*40, end="\n\n")
#############################

print("2. Enclosed Scope")
print("-"*20)
# -----------


def f1():
    x = 100 # Since it is being used in nested function as well
    # So this variable is in ENCLOSED
    def f2():
        print("Accessing outer function variable", x)


print("#"*40, end="\n\n")
#############################


print("3. Global Scope")
print("-"*20)
# -----------


y = 10 # Global Scope: We can access anywhere
def f1():
    print("Accessing global y is f1():", y)
    def f2():
        print("Accessing global y is f2():", y)


print("#"*40, end="\n\n")
#############################

print("4. Builtin Scope")
print("-"*20)
# -----------

# 1st check in local scope
# if not present
# then check enclosed scope
# if not present
# then check Global scope
# if not present
# then check Builtins


print("#"*40, end="\n\n")
#############################


print("We can change GLOBAL variable value inside function")
print("-"*20)
# -----------
my_global_var_value = 100
def f1():
    global my_global_var_value
    my_global_var_value = 2000

print("my_global_var_value:", my_global_var_value) # 100
f1()
print("my_global_var_value:", my_global_var_value) # 2000

print("#"*40, end="\n\n")
#############################

print("We can change ENCLOSED variable value inside function")
print("-"*20)
# -----------


def main_function():
    main_func_variable = 100
    def nested_function():
        nonlocal main_func_variable
        main_func_variable = 2000
    print("main_func_variable before:", main_func_variable)
    nested_function()
    print("main_func_variable after:", main_func_variable)

main_function()

print("#"*40, end="\n\n")
#############################