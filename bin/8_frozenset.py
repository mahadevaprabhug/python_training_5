"""
Frozenset:
    -- We have option to store multiple values like list of employee names
    -- We can store UNIQUE values
    -- No index to each value
    -- We can keep only immutable values like numbers, str, tuple
        We can't store mutable values like list, dict, set etc
    -- order values also not maintained
"""

print("Frozenset part-1")
print("Store the values")
print("-"*20)
# -----------

# No shortcut for frozenset, we need to use class name to create object
my_fs = frozenset([10, 10, "python", "python", "java", "java"])
print(my_fs)

# Since we dont have index,
# If we want to access individual values
# either convert to other type like list/tuple
# OR using loop we can iterate
data_in_list = list(my_fs)
print("data_in_list:", data_in_list)

print("#"*40, end="\n\n")
#############################

print("Methods present inside 'frozenset' class")
print("-"*20)
# -----------

print(dir(frozenset))

print("#"*40, end="\n\n")
#############################

print("union, intersection, difference methods")
print("-"*20)
# -----------

sb_acc_customers = frozenset(["cust-1", "cust-2", "cust-3", "cust-4"])
loan_acc_customers = frozenset(["cust-3", "cust-4", "cust-5", "cust-6"])

print("sb_acc_customers:", sb_acc_customers)
print("loan_acc_customers:", loan_acc_customers, end="\n\n")

all_customers = sb_acc_customers.union(loan_acc_customers)
print("all_customers:", all_customers)

customers_having_both_loan_sb = sb_acc_customers.intersection(loan_acc_customers)
print("customers_having_both_loan_sb:", customers_having_both_loan_sb)

customers_not_having_loan = sb_acc_customers.difference(loan_acc_customers)
print("customers_not_having_loan:", customers_not_having_loan)

print("#"*40, end="\n\n")
#############################
