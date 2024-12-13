"""
while-loop: Execute loop based on the condition
"""

print("while-loop: Execute loop based on the condition")
print("-"*20)
# -----------

x = 0
while x < 5:
    print("Value x is:", x)
    x = x + 1

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

index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Course Java Found")
        break
    index_no = index_no + 1

# for each_value in my_list:
#     if each_value.startswith("Java"):
#         print("Course Java Found")
#         break


print("#"*40, end="\n\n")
#############################

print("# Case-2: 'continue statement': How to skip/jump to next iteration in between")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    if not my_list[index_no].startswith("Java"):
        index_no = index_no + 1 # index_no += 1
        continue # goto next iteration
    # Below code till end of the block is applicable for only Java course
    # OR other than java courses are not required from this line onwards
    print("This Java Course name is:", my_list[index_no])
    print("This is one version of Java")
    print("This java course duration is 10 days", end="\n\n")
    index_no += 1

# for each_course in my_list:
#     if not each_course.startswith("Java"):
#         continue # goto next iteration
#     # Below code till end of the block is applicable for only Java course
#     # OR other than java courses are not required from this line onwards
#     print("This Java Course name is:", each_course)
#     print("This is one version of Java")
#     print("This java course duration is 10 days", end="\n\n")


print("#"*40, end="\n\n")
#############################

print("while-else block")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    print("Each Course:", my_list[index_no])
    index_no += 1
    # break # if we break, then else will not execute
else:
    print("Reached for-else")
    print("some cleanup.. here making my_list empty because those values are not required")
    # my_list.clear()
    # OR
    del my_list


# for each_course in my_list:
#     print("Each course:", each_course)
#     # break
# else:
#     print("Reached for-else")
#     print("some cleanup.. here making my_list empty because those values are not required")
#     # my_list.clear()
#     # OR
#     del my_list

# Behavior of while-else
# while-else: After executing while-loop, 'else' block will execute
# while-else: if we are ending while-loop using 'break'. It will come out
#   of while-block and 'else-block'

print("#"*40, end="\n\n")
#############################
