"""
Exceptions Handling
"""

# print("WITHOUT handling exception: Program will terminate abruptly")
# print("-"*20)
# # -----------
#
# a = 10
# b = 0
# result = a / b # Program will terminate here abruptly
# print("result:", result)
#
# print("#"*40, end="\n\n")
# #############################

print("Handling Exceptions")
print("-"*20)
# -----------

try:
    # Keep code here which we are planning monitor for error
    # If some error comes in this block, then program will not terminate
    #   instead control will be passed to except block
    #
    # If no error in this block then except block will be skipped
    pass
except:
    # Here we will write code to solve error occurred in try block
    pass

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate here. Instead control will be passed to except block
    print("result:", result) # Remaining statements in this block will never execute
except:
    print("Reched except block because there is in error in try")

print("#"*40, end="\n\n")
#############################

# About 'Exception' classes
# -----------
# - If we want to handle exceptions using 'try-except'
#   then we need to have exception class for that error
#   If not, we can't handle
#   If we can't handle then program will terminate with error
#
# - We have some error classes in builtins which we can make use
#
# - If we are using some library may provide error classes to handle error
#   occurred while using that library
#
# - For remaining, we need to write our own exception classes
#
# - Default 'except' block will be able receive all type of errors
#   which has error class
#
# - Main class or super class for all exception class is 'Exception'
#############################

print("Handling Exceptions with class names in except block")
print("-"*20)
# -----------

try:
    a = 10
    b = 0
    result = a / xyz  # variable xyz is not defined
    print("result:", result) # Remaining statements in this block will never execute
except ZeroDivisionError: # 1-way just mention class name
    print("Reched except block because there is in error in try")
    print("This ZDE block")
except NameError as ne: # 2-way capture error class object
    print("Reched except block because there is in error in try")
    print("This NE block and value of ne is:", ne)

print("#"*40, end="\n\n")
#############################

print("WITHOUT using 'try-except-else'")
print("-"*20)
# -----------


try:
    try:
        print("Reached nested try block")
        my_file_handle = open(r"C:\sndksd.txt", "r")
    except FileNotFoundError:
        print("Reached nested 'except'. it is file not found error")
        print("Can't Proceed")
        # exit()
    try:
        print("Reached nested 2nd try block")
        file_content = my_file_handle.read()
        my_file_handle.close()
    except Exception as e:
        print("Not able read file content because of errror: ", e)
except Exception as e:
    print("Some error while doing file operations:", e)

print("#"*40, end="\n\n")
#############################

print("Using 'try-except-else' Same example")
print("-"*20)
# -----------


try:
    print("Reached nested try block")
    my_file_handle = open(r"C:\sndksd.txt", "r")
except:
    print("Reached nested 'except'. it is file not found error")
else:
    print("Reached Else block")
    file_content = my_file_handle.read()
    my_file_handle.close()

# 'else' block is continuation of 'try' block
# if 'try' success then 'else' block will execute
#   and 'except' block will be skipped
# if 'try' failed then 'except' block will execute
#   and 'else' block will be skipped

print("#"*40, end="\n\n")
#############################

print("Using 'try-except-else-finally' ")
print("-"*20)
# -----------


try:
    print("Reached nested try block")
    my_file_handle = open(r"C:\sndksd.txt", "r")
except:
    print("Reached nested 'except'. it is file not found error")
    print("Can't Proceed")
    # exit()
else:
    print("Reached nested 2nd try block")
    file_content = my_file_handle.read()
finally:
    print("Reached finally block")
    try:
        my_file_handle.close()
    except Exception as e:
        print("Not able to close file handle because :", e)

# 'finally' block will execute even if 'try/except/else'
#   blocks success/failed. in both the cases finally will execute
#


print("#"*40, end="\n\n")
#############################


print("User Defined Exception Class Example-1")
print("-"*20)
# -----------

# Mandatory Step: Our class should be subclass of 'Exception' class
#   OR if some class are already subclass of 'Exception' class
#   like all built exception classes are subclass of 'Exception'
#   then we can also extend those classes

class MyError(Exception):
    pass
# It is valid class, using this class we can handle using 'try-except'

try:
    x = 10
    if x == 10:
        raise MyError
    if x > 10:
        raise MyError
    if x < 10:
        raise MyError
except MyError:
    print("Reached 'MyError' except block")


print("#"*40, end="\n\n")
#############################

print("INFO:User Defined Exception Class Example-2")
print("-"*20)
# -----------

# Requirement: send some message while raising error

class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg

    def get_error_message(self):
        return self.error_message


try:
    x = 10
    if x == 10:
        raise MyError("Here value of x is 10 so raising MyError")
    if x > 10:
        raise MyError("Here value of x is gt 10 so raising MyError")
    if x < 10:
        raise MyError("Here value of x is lt 10 so raising MyError")
except MyError as m:
    print("Reached 'MyError' except block Error Details:", m.error_message)
    print("OR")
    print("Reached 'MyError' except block Error Details:", m.get_error_message())


print("#"*40, end="\n\n")
#############################
