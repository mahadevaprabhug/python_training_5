"""
- Tuple:
    -- We have option to store multiple values like list of employee names
    -- We can store duplicate values
    -- Automatically index number will be assigned to each value
"""

print("Tuple PART-1")
print("Store multiple values")
print("-"*20)
# -----------

my_tuple = (10, 12.5, "python", (100, 200))
# it will create object of builtin class 'tuple' and store the values
print("my_tuple:", my_tuple)
print("type of my_tuple:", type(my_tuple))

print("#"*40, end="\n\n")
#############################

print("Tuple PART-2")
print("Indexing/slicing is similar to string")
print("-"*20)
# -----------

my_tuple = (10, 12.5, "python", (100, 200, "Java"))
print("my_tuple:", my_tuple)

print("Course Name:", my_tuple[2]) # 'python'
print("Type Course Name:", type(my_tuple[2]))
print("2nd character in Course Name:", my_tuple[2][1], end="\n\n") # 'y'

print("Nested tuple:", my_tuple[3]) # (100, 200, "Java")
print("Course name:", my_tuple[3][-1]) # "Java"
print("2nd char in Course name:", my_tuple[3][-1][1]) # "a"

print("#"*40, end="\n\n")
#############################

print("Methods inside 'tuple' class")
print("-"*20)
# -----------

print(dir(my_tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
#############################

print("Getting help:")
print("-"*20)
# -----------

print(help(my_tuple.index))

print("#"*40, end="\n\n")
#############################


print("'index' and 'count' method")
print("-"*20)
# -----------

my_tuple = (10, 12.5, "python", (100, 200, "Java"))
print("my_tuple:", my_tuple, end="\n\n")

index_of_python = my_tuple.index("python")
print("index_of_python:", index_of_python, end="\n\n")

nested_tuple = my_tuple[3] # (100, 200, "Java")
index_of_java = nested_tuple.index("Java")
# OR
index_of_java = my_tuple[3].index("Java")
print("index_of_java:", index_of_java, end="\n\n")

count_of_python = my_tuple.count("python")
print("count_of_python:", count_of_python, end="\n\n")

print("#"*40, end="\n\n")
#############################
