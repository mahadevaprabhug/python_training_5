"""
Dictionary:
    -- We have option to store multiple values like list of employee names
    -- We can store duplicate values
    -- We can provide index to each value: KEY/VALUE pair
"""

print("Dictionary PART-1")
print("Store the values")
print("-"*20)
# -----------

my_dictionary_1 = {0:"python", 1:10, 2:"online"}
# It will create object of 'dict' class and store the values

# FOR KEYS: We can use any IMMUTABLE values like numbers, string, tuple
my_dictionary_2 = {"course":"python", "duration":10, "mode":"online"}

# FOR VALUES: We can store any type of values
my_dictionary_3 = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1, end="\n\n")
print("my_dictionary_2:", my_dictionary_2, end="\n\n")
print("my_dictionary_3:", my_dictionary_3, end="\n\n")

print("#"*40, end="\n\n")
#############################

print("Dictionary PART-2")
print("We can access individual values")
print("-"*20)
# -----------

my_dictionary = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n") # 10

course_name = my_dictionary["course"]
print("course_name:", course_name)# "python"
print("2nd char in course_name:", course_name[1])# "y"
print("2nd char in course_name 2-way to access:", my_dictionary["course"][1], end="\n\n")# "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("last Mode:", my_dictionary["mode"][-1]) # "offline"
print("4th char in last Mode:", my_dictionary["mode"][-1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("Trainer LName:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd char in Trainer LName:", my_dictionary["trainer"]["lname"][1], end="\n\n") # "y"

print("#"*40, end="\n\n")
#############################

print("Dictionary PART-3")
print("Methods present inside 'dict' class")
print("-"*20)
# -----------

print(dir(dict))

print("#"*40, end="\n\n")
#############################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# -----------

my_dictionary = {"course":"python", "duration":10, "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# ADD/UPDATE : If key present then update else add
my_dictionary["location"] = "India" # Here it will add
print("my_dictionary after updating location:", my_dictionary, end="\n\n")

other_dictionary = {"A": 10, "location": "XYZ"}
print("other_dictionary:", other_dictionary)
my_dictionary.update(other_dictionary) # If key present then update else add
print("my_dictionary after updating other_dictionary:", my_dictionary, end="\n\n")

# Remove
my_dictionary.pop("course")
print("my_dictionary after removing course:", my_dictionary, end="\n\n")

my_dictionary.popitem()
print("my_dictionary after removing last value:", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
#############################
