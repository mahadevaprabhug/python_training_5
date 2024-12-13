"""
- Strings:
    -- We have option to store text data like word, sentence, name, email etc
    -- Automatically index number will be assigned to each character
"""

print("Strings PART-1")
print("How to store values")
print("-"*20)
# -----------

a = 'PERSON'
b = 'PERSON\'S'
c = "PERSON'S"
d = """PERSON'S HEIGHT IS XYZ" (" represents inch)"""
e = '''PERSON'S HEIGHT IS XYZ" (" represents inch)'''

print(a, b, c, d, e, sep="\n")

print("#"*40, end="\n\n")
#############################

print("Strings PART-2")
print("How to store values")
print("-"*20)
# -----------

a = "C:\newfolder\test.py"
# Default \n\t will get replaced with new line & tab space
print("Value of a=", a, end="\n\n")

b = r"C:\newfolder\test.py"
# r -> RAW string, it will keep \n\t as it is
print("Value of b=", b, end="\n\n")

print("Converting non-raw format of the string (which is a) to raw-string:", repr(a))

print("#"*40, end="\n\n")
#############################


print("Strings PART-3")
print("How to store values")
print("-"*20)
# -----------

x = 10
y = 20
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f -> format: It will replace {var_name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
#############################


print("Strings PART-4")
print("Access each character using index number")
print("-"*20)
# -----------
# In all the above cases, it will create object of builtin class 'str'
# and store the values

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print("0th character using +ve index number:", my_string[0])
print("0th character using -ve index number:", my_string[-8])

# print("100th character using +ve index number:", my_string[100]) # ERROR

print("#"*40, end="\n\n")
#############################

print("Strings PART-5")
print("Slicing: We can get substring")
print("-"*20)
# -----------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print("substring from index-1 to 6 using +ve index number:", my_string[1:6])
print("substring from index-1 to 6 using -ve index number:", my_string[-7:-2])
print("substring from index-1 to 6 using -ve/+ve index number:", my_string[1:-2])
print("substring from index-1 to 6 using -ve/+ve index number:", my_string[-7:6], end="\n\n")

print("substring from index-1 to END using +ve index number:", my_string[1:])
print("substring from index-1 to END using -ve index number:", my_string[-7:], end="\n\n")

print("substring from BEGINNING to 6 using +ve index number:", my_string[:6])
print("substring from BEGINNING to 6 using -ve index number:", my_string[:-2], end="\n\n")

print("#"*40, end="\n\n")
#############################

print("Strings PART-6")
print("Step Value: We can skip characters in between")
print("-"*20)
# -----------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print("substring from index-1 to 6 using + ve index number with default step value 1:", my_string[1:6])
print("substring from index-1 to 6 using - ve index number with default step value 1:", my_string[-7:-2], end="\n\n")
# step value 1, which means, from 1 to 6 give me every character
# here start character will always come & char at end index will not come

print("substring from index-1 to 6 using + ve index number with step value 1:", my_string[1:6:1])
print("substring from index-1 to 6 using - ve index number with step value 1:", my_string[-7:-2:1], end="\n\n")
# step value 1, which means, from 1 to 6 give me every character
# here start character will always come & char at end index will not come

print("substring from index-1 to 6 using + ve index number with step value 2:", my_string[1:6:2])
print("substring from index-1 to 6 using - ve index number with step value 2:", my_string[-7:-2:2], end="\n\n")
# step value 2, which means, from 1 to 6 give me every 2nd character
# here start character will always come & char at end index will not come

print("#"*40, end="\n\n")
#############################

print("Strings PART-7")
print("-ve Step Value: We can traverse in reverse direction")
print("-"*20)
# -----------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Example: 6 to 1 in reverse
# then mandataory steps
# step-1: start index should be 6
# step-2: end index should be 1
# step-3: step value should be -ve value like -1, -2 etc
# ALL 3 STEPS ARE MANDATORY

print("Substring from 6 to 1 using + ve index number with step value -1:", my_string[6:1:-1])
print("Substring from 6 to 1 using - ve index number with step value -1:", my_string[-2:-7:-1], end="\n\n")

print("Substring from 6 to 1 using + ve index number with step value -2:", my_string[6:1:-2])
print("Substring from 6 to 1 using - ve index number with step value -2:", my_string[-2:-7:-2], end="\n\n")

print("#"*40, end="\n\n")
#############################

print("List of methods & variables present in 'str' class")
print("-"*20)
# -----------

print(dir(my_string))
# OR
# print(dir(str))

# About __ names
# ------------
# - these are system defined names
# - these are mapped to either operator or some function
# - Example-1:
#   my_string[0] -> internally it will call my_string.__getitem__(0)
#   So, [] mapped to __getitem__
#
# Example-2:
#   s1 = "Hello"
#   s2 = "hi"
#   s1 + s2 -> internally it will call __add__
#
##################

print("#"*40, end="\n\n")
#############################

print("Trying 'startswith' method")
print("-"*20)
# -----------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

starts_with_result = my_string.startswith("WEL") # True/False
print("starts_with_result:", starts_with_result) # True

print("#"*40, end="\n\n")
#############################

print(help(my_string.startswith))