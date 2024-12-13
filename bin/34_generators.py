"""
Generator: We can create value/object whenever we want OR on the fly we can
create value/object.
"""

print("Without using Generators")
print("-"*20)
# -----------


def my_square_function(my_list):
    square_result = []
    for i in my_list:
        square_result.append(i*i)
    return square_result

L = [10, 20, 30, 40, 50]

func_result = my_square_function(L)

print("func_result:", func_result, end="\n\n")

for i in func_result:
    print("Value of i:", i)


print("#"*40, end="\n\n")
#############################

# Above block Requirement
# -----------
# - Requirement is to print one value at a time using for-loop
# - Currently, function is keeping all the squared values created
#   and stored in list. for loop is using that list
#
# OBSERVATION: Even though for-loop need one value at a time, we
#   are keeping all squared values in list which is occupying memory
#
#############################


# Requirement:
# -----------
# - Are there any way where we can obtain/create value/object
#   whenever we want. Instead of keeping all squared values in list
#
# - ONE TIME USE is enough
#############################


print("Using Generators")
print("-"*20)
# -----------


def my_square_generator_function(my_list):
    for i in my_list:
        yield i * i

L = [10, 20, 30, 40, 50]

func_result = my_square_generator_function(L)
print("func_result:", func_result, end="\n\n")

for i in func_result:
    print("Value of i:", i)


print("#"*40, end="\n\n")
#############################
