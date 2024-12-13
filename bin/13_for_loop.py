"""
for-loop: Iterate any collection like str, list, etc
"""

print("for-loop: Iterate any collection like str, list, etc")
print("-"*20)
# -----------

my_string = "Python"
print("my_string:", my_string)
for i in my_string:
    print("Each Char in my_string:", i)

print("\n")

my_list = ["Java", "C++", "python", (100,200)]
print("my_list:", my_list)
for i in my_list:
    print("Each Value in my_list:", i)


print("\n")

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# dict_keys(['course', 'duration', 'mode'])
for k in my_dictionary.keys():
    print("Each key using my_dictionary.keys():", k)
    print("Value of that key:", my_dictionary[k])

print("\n")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]
# >>>
for i in my_dictionary.items():
    print("Each tuple in my_dictionary.items():", i)
    print("key:", i[0])
    print("Value:", i[1])

print("\n")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]
# >>>
for i, j in my_dictionary.items():
    print("Using 2nd way, Key is:", i)
    print("Using 2nd way, Value is:", j)

print("#"*40, end="\n\n")
#############################

print("Nested for-loop")
print("-"*20)
# -----------

my_list = ["Java", "C++", "python", (100,200)]
print("my_list:", my_list)
for i in my_list:
    if type(i).__name__ == 'str':
        for j in i:
            print("Each char in string using nested for-loop:", j)
    elif type(i).__name__ == 'tuple':
        for j in i:
            print("Each value in tuple using nested for-loop:", j)
    else:
        print("printing as it is and value is:", i)


# Example:
# >>> T =(100,200)
# >>> type(T)
# <class 'tuple'>
# >>> type(T).__name__
# 'tuple'
# >>>
print("#"*40, end="\n\n")
#############################

# 2 Cases
# Case-1: 'break statement': How to end for-loop in between
# Case-2: 'continue statement': How to skip/jump to next iteration in between

print("# Case-1: 'break statement': How to end for-loop in between")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

# Requirement: Verify are there any value starting with Java
for each_value in my_list:
    if each_value.startswith("Java"):
        print("Course Java Found")
        break


print("#"*40, end="\n\n")
#############################


print("# Case-2: 'continue statement': How to skip/jump to next iteration in between")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

for each_course in my_list:
    if not each_course.startswith("Java"):
        continue # goto next iteration
    # Below code till end of the block is applicable for only Java course
    # OR other than java courses are not required from this line onwards
    print("This Java Course name is:", each_course)
    print("This is one version of Java")
    print("This java course duration is 10 days", end="\n\n")


print("#"*40, end="\n\n")
#############################

print("for-else block")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

for each_course in my_list:
    print("Each course:", each_course)
    # break
else:
    print("Reached for-else")
    print("some cleanup.. here making my_list empty because those values are not required")
    # my_list.clear()
    # OR
    del my_list

# Behavior of for-else
# for-else: After executing for-loop, 'else' block will execute
# for-else: if we are ending for-loop using 'break'. It will come out
#   of for-block and 'else-block'

print("#"*40, end="\n\n")
#############################
