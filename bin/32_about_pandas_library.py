"""
About pandas
- pandas is a library
- pandas is having many functions and many classes
    Few Function Names: read_csv, read_excel etc
    Few Class Names: DataFrame, Series etc


About DataFrame class
- DataFrame is MAIN class
- It has methods related to tabular data operations
"""

print("Inside pandas library")
print("-"*20)
# -----------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
#############################

print("Inside 'DataFrame' class")
print("-"*20)
# -----------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
#############################

print("Storing Values: Example-1")
print("-"*20)
# -----------

my_df = pd.DataFrame([[10, 20, 30, 40],[50, 60, 70, 80],[90, 100, 200, 300]])
print(my_df)

print("#"*40, end="\n\n")
#############################

print("Storing Values: Example-2")
print("-"*20)
# -----------

my_df = pd.DataFrame([[10, 20, 30, 40],[50, 60, 70, 80],[90, 100, 200, 300]],
                     index=["r1", "r2", "r3"],
                     columns=["c1", "c2", "c3", "c4"]
                     )
print(my_df)

print("#"*40, end="\n\n")
#############################
