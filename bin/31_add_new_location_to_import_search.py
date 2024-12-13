"""
Adding new location to import search list. where we are keeping our libraries
like mymodule.py, mypackage
"""

print("Default list of directories where 'import' will search")
print("-"*20)
# -----------

import sys
print(sys.path)

print("#"*40, end="\n\n")
#############################

print("Adding new location to import search list")
print("-"*20)
# -----------

import sys
sys.path.append(r"D:\mylib1")
sys.path.insert(0,r"D:\mylib2") # add at index-0

print("#"*40, end="\n\n")
#############################

print("After adding new location")
print("-"*20)
# -----------

print(sys.path)

print("#"*40, end="\n\n")
#############################
