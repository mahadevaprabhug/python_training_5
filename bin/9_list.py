"""
MUTABLE
- list:
    -- We have option to store multiple values like list of employee names
    -- We can store duplicate values
    -- Automatically index number will be assigned to each value
"""

print("list PART-1")
print("Store multiple values")
print("-"*20)
# -----------

my_list = [10, 12.5, "python", (100, 200)]
# it will create object of builtin class 'list' and store the values
print("my_list:", my_list)
print("type of my_list:", type(my_list))

print("#"*40, end="\n\n")
#############################

print("list PART-2")
print("Indexing/slicing is similar to string")
print("-"*20)
# -----------

my_list = [10, 12.5, "python", (100, 200, "Java")]
print("my_list:", my_list)

print("Course Name:", my_list[2]) # 'python'
print("Type Course Name:", type(my_list[2]))
print("2nd character in Course Name:", my_list[2][1], end="\n\n") # 'y'

print("Nested list:", my_list[3]) # (100, 200, "Java")
print("Course name:", my_list[3][-1]) # "Java"
print("2nd char in Course name:", my_list[3][-1][1]) # "a"

print("#"*40, end="\n\n")
#############################

print("Methods inside 'list' class")
print("-"*20)
# -----------

print(dir(my_list))
# OR
# print(dir(list))

print("#"*40, end="\n\n")
#############################

print("Getting help:")
print("-"*20)
# -----------

print(help(my_list.index))

print("#"*40, end="\n\n")
#############################


print("'index' and 'count' method")
print("-"*20)
# -----------

my_list = [10, 12.5, "python", (100, 200, "Java")]
print("my_list:", my_list, end="\n\n")

index_of_python = my_list.index("python")
print("index_of_python:", index_of_python, end="\n\n")

nested_list = my_list[3] # (100, 200, "Java")
index_of_java = nested_list.index("Java")
# OR
index_of_java = my_list[3].index("Java")
print("index_of_java:", index_of_java, end="\n\n")

count_of_python = my_list.count("python")
print("count_of_python:", count_of_python, end="\n\n")

print("#"*40, end="\n\n")
#############################

print("ADD/REMOVE/UPDATE")
print("-"*20)
# -----------

my_list = [10, 12.5, "python", (100, 200, "Java")]
print("my_list:", my_list, end="\n\n")

# ADD
my_list.append("C++") # [10, 12.5, "python", (100, 200, "Java"), "C++"]
print("my_list after appending C++:", my_list, end="\n\n")

# Remove
my_list.pop(3) # [10, 12.5, "python", "C++"]
print("my_list after deleting inner tuple:", my_list, end="\n\n")

# Update
my_list[1] = "Java" # [10, "Java", "python", "C++"]
print("my_list after updating 12.5 to Java:", my_list, end="\n\n")

print("#"*40, end="\n\n")
#############################
