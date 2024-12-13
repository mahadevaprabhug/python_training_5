"""
Conditional Block 'if': We can execute block of code based on condition
"""

print("multiple if-block")
print("-"*20)
# -----------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

if x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

if x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
#############################

print("if-elif blocks")
print("-"*20)
# -----------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

elif x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
#############################

print("if-elif-else blocks")
print("-"*20)
# -----------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

else:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
#############################

print("'if' with str, list, or any other collections")
print("-"*20)
# -----------

my_string = "Python"
print("my_string:", my_string)
if (my_string != "Java") and ("tho" in my_string):
    print("All conditions True for my_string", end="\n\n")


my_list = ["Java", "C++", "python", (100,200)]
print("my_list:", my_list)
if ("C++" in my_list) and ((100, 200) in my_list):
    print("Values are found in my_list", end="\n\n")


my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# dict_keys(['course', 'duration', 'mode'])
if "course" in my_dictionary.keys():
    print("Key 'course' found")

# >>> my_dictionary.values()
# dict_values(['python', 10, 'online'])
# >>>
if 'python' in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# dict_items([('course', 'python'), ('duration', 10), ('mode', 'online')])
# >>>
if ('course', 'python') in my_dictionary.items():
    print("Both key value present")


print("#"*40, end="\n\n")
#############################