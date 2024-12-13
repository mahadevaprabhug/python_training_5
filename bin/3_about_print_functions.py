"""
About print function
"""

print("print function with 'sep'")
# print("----------------")
print("-"*20)
# -------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # Default sep="ONE SPACE"
print(a, b, c, d, sep="X")
print(a, b, c, d, sep="\t\t")

print("#"*40)
###########################

print("print function with 'end'")
print("-"*20)
# -------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # Default end="\n": Put \n at the end
print(a, b, c, d) #
print(a, b, c, d)

print(a, b, c, d, end="\t\t")
print(a, b, c, d, end="XYZ")
print(a, b, c, d, end="ABC\n")

# file parameter: We will discuss during file operations

print("#"*40)
###########################
