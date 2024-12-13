"""
set:
    -- We have option to store multiple values like list of employee names
    -- We can store UNIQUE values
    -- No index to each value
    -- We can keep only immutable values like numbers, str, tuple
        We can't store mutable values like list, dict, set etc
    -- order values also not maintained
"""

print("set part-1")
print("Store the values")
print("-"*20)
# -----------

my_set = {10, 10, "python", "python", "java", "java"}
print(my_set)

my_set = set([10, 10, "python", "python", "java", "java"])
print(my_set)

# Since we dont have index,
# If we want to access individual values
# either convert to other type like list/tuple
# OR using loop we can iterate
data_in_list = list(my_set)
print("data_in_list:", data_in_list)

print("#"*40, end="\n\n")
#############################

print("Methods present inside 'set' class")
print("-"*20)
# -----------

print(dir(set))

print("#"*40, end="\n\n")
#############################

print("union, intersection, difference methods")
print("-"*20)
# -----------

sb_acc_customers = set(["cust-1", "cust-2", "cust-3", "cust-4"])
loan_acc_customers = set(["cust-3", "cust-4", "cust-5", "cust-6"])

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

print("ADD/REMOVE/UPDATE")
print("-"*20)
# -----------

sb_acc_customers_set_1 = {"cust-1", "cust-2", "cust-3", "cust-4"}
print("sb_acc_customers_set_1:", sb_acc_customers_set_1, end="\n\n")

# Add
sb_acc_customers_set_1.add("cust-5")
print("sb_acc_customers_set_1 after adding cust-5:", sb_acc_customers_set_1, end="\n\n")

# Remove
sb_acc_customers_set_1.remove("cust-2")
print("sb_acc_customers_set_1 after removing cust-2:", sb_acc_customers_set_1, end="\n\n")

# Update
sb_acc_customers_set_2 = {"cust-3", "cust-4", "cust-5", "cust-6"}
print("sb_acc_customers_set_2:", sb_acc_customers_set_2, end="\n\n")
sb_acc_customers_set_1.update(sb_acc_customers_set_2)
print("sb_acc_customers_set_1 after updating sb_acc_customers_set_2:", sb_acc_customers_set_1)

print("#"*40, end="\n\n")
#############################
