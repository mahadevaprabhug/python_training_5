"""
Text File Operations (Read and write to text file like .txt, .log)
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read/Write
    - FOR WRITING: 1) write 2) writelines 3) print-function
    - FOR READING: 1) read 2) readline 3) readlines
Step-3: Disconnect
    - close() function
"""

print("All write operations")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
# my_out_file_handle = open("provide file name or file path here", "provide mode")
# w -> write -> it will create file -> it will erase the content if already present
# r-> read -> it will not create new file if file not present
# a -> append -> It will create file only if file not present
#
# 'w+', 'r+', 'a+' : We can do both Read&Write
#
# 'wb', 'rb', 'ab' : We can do both Read&Write
#
my_out_file_handle = open("my_out_file.txt", "w")

# Step-2: Write
# -----------

# Our data
x = 10
y = "python"

# 1) write: We can pass only one string of any length
my_out_file_handle.write(str(x)+"\n")
my_out_file_handle.write(y+"\n")

# 2) writelines: collection of strings
L = [str(x)+"\n", y+"\n"]
my_out_file_handle.writelines(L)

# 3) print-function
print(x, y, 20, "java", sep="\n", file=my_out_file_handle)

# Step-3: Disconnect
# -----------
my_out_file_handle.close()

print("""
Created my_out_file.txt, 
Please check
""")

print("#"*40, end="\n\n")
#############################

print("Reading from file using read()")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -----------
file_content = my_out_file_handle.read()
# returns entire file content in one string
print("file_content:", file_content, end="\n\n")
print("file_content in raw format:", repr(file_content), end="\n\n")

# Step-3: Disconnect
# -----------
my_out_file_handle.close()

print("#"*40, end="\n\n")
#############################

print("Reading from file using readlines()")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -----------
file_content = my_out_file_handle.readlines()
# returns entire file content in list
print("file_content:", file_content)

# Step-3: Disconnect
# -----------
my_out_file_handle.close()

print("#"*40, end="\n\n")
#############################

print("Reading from file using readline()")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -----------
file_content = my_out_file_handle.readline()
print("1st line:", file_content)

file_content = my_out_file_handle.readline()
print("2nd line:", file_content)

file_content = my_out_file_handle.readline()
print("3rd line:", file_content)

# Step-3: Disconnect
# -----------
my_out_file_handle.close()

print("#"*40, end="\n\n")
#############################

print("Reading from file using for-loop to read line by line")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -----------
for each_line in my_out_file_handle:
    print("Each line:", each_line)

# Step-3: Disconnect
# -----------
my_out_file_handle.close()

print("#"*40, end="\n\n")
#############################
