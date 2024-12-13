"""
PACKAGES: If we are developing more and more modules then
we can keep/organize in folders & sub-folders.

These folders are also called PACKAGES or PYTHON-LIBRARY
"""

print("1-way: using 'import'")
print("-"*20)
# -----------

import mypackage.db.mymodule
print("Course:", mypackage.db.mymodule.course)

add_result = mypackage.db.mymodule.add(10, 20)
print("add_result:", add_result)

e1 = mypackage.db.mymodule.Employee("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
#############################

print("2-way: using 'from-import'")
print("-"*20)
# -----------

from mypackage.db.mymodule import course, add, Employee
print("Course:", course)

add_result = add(10, 20)
print("add_result:", add_result)

e1 = Employee("emp-1")
print("Employee Name:", e1.get_name())


print("#"*40, end="\n\n")
#############################


print("1-way: using 'import' Using Short Name")
print("-"*20)
# -----------

import mypackage.db.mymodule as mm
print("Course:", mm.course)

add_result = mm.add(10, 20)
print("add_result:", add_result)

e1 = mm.Employee("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
#############################

print("2-way: using 'from-import' Using Short Name")
print("-"*20)
# -----------

from mypackage.db.mymodule import course as c, add as a, Employee as E
print("Course:", c)

add_result = a(10, 20)
print("add_result:", add_result)

e1 = E("emp-1")
print("Employee Name:", e1.get_name())


print("#"*40, end="\n\n")
#############################
