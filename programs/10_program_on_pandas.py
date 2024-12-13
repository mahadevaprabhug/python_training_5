"""
Get data from 2 sources
1. my_database.sqlite3
2. log_process_class_report.json

and
write to files

df_report.csv
df_report.xlsx
df_report.json
df_report.xml
"""

print("Get data from db")
print("-"*20)
# -----------

import sqlite3
my_db_connection = sqlite3.connect("my_database.sqlite3")

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)
print(my_db_df)

print("#"*40, end="\n\n")
#############################

print("Column names")
print("-"*20)
# -----------

print(my_db_df.columns)
# ['IP', 'DATE', 'PICS', 'URL']

print("#"*40, end="\n\n")
#############################

print("PICS Column")
print("-"*20)
# -----------

print(my_db_df["PICS"])
# my_db_df.iloc[row_index,column_index]
# For PICS -> my_db_df.iloc[:,2] # All rows, 3rd column

print("#"*40, end="\n\n")
#############################

print("Get data from json file")
print("-"*20)
# -----------

my_json_df = pd.read_json("log_process_class_report.json")
print(my_json_df)

print("#"*40, end="\n\n")
#############################


print("Rotate json DataFrame")
print("-"*20)
# -----------

my_json_df = my_json_df.T
print(my_json_df)

print("#"*40, end="\n\n")
#############################

print("json data columns")
print("-"*20)
# -----------

print(my_json_df.columns)

print("#"*40, end="\n\n")
#############################

print("Give name to json data columns")
print("-"*20)
# -----------
my_json_df.columns = ["IP", "PICS"]
print(my_json_df.columns)

print("#"*40, end="\n\n")
#############################

print("json data df after naming columns")
print("-"*20)
# -----------

print(my_json_df)

print("#"*40, end="\n\n")
#############################


print("Merge both DB and Json DataFrame")
print("-"*20)
# -----------

merged_df = pd.concat([my_db_df, my_json_df], axis=0)
print(merged_df)

print("#"*40, end="\n\n")
#############################


print("Merged data in intermediate_merged.csv file")
print("-"*20)
# -----------

merged_df.to_csv("intermediate_merged.csv")
print("created intermediate_merged.csv, please check")


print("#"*40, end="\n\n")
#############################

print("Null cells")
print("-"*20)
# -----------

print(merged_df.isnull())

print("#"*40, end="\n\n")
#############################

print("Total null cells")
print("-"*20)
# -----------

print(merged_df.isnull().sum())

print("#"*40, end="\n\n")
#############################

print("Total null cells in DATE Column")
print("-"*20)
# -----------

print(merged_df["DATE"].isnull().sum())

print("#"*40, end="\n\n")
#############################


print("Fill DATE column null values with '26-04-2000'")
print("-"*20)
# -----------

merged_df["DATE"] = merged_df["DATE"].fillna('26-04-2000')
print(merged_df)

print("#"*40, end="\n\n")
#############################

print("Fill URL column null values with 'http://www.jafsoft.com/asctortf/'")
print("-"*20)
# -----------

merged_df["URL"] = merged_df["URL"].fillna('http://www.jafsoft.com/asctortf/')
print(merged_df)

print("#"*40, end="\n\n")
#############################

print("Creating Final Reports")
print("-"*20)
# -----------

# df_report.csv
merged_df.to_csv("df_report.csv", index=False)

# df_report.xlsx
merged_df.to_excel("df_report.xlsx", index=False)

# df_report.json
# merged_df.to_json("df_report.json")

# df_report.xml
merged_df.to_xml("df_report.xml")

print("""
Created Below Files, 
Please Check

df_report.csv
df_report.xlsx
df_report.xml

""")

print("#"*40, end="\n\n")
#############################

print("Before Resetting Index")
print("-"*20)
# -----------

print(merged_df)

print("#"*40, end="\n\n")
#############################

print("After Resetting Index")
print("-"*20)
# -----------

# merged_df = merged_df.reset_index()
merged_df = merged_df.reset_index(drop=True) # Drop existing index column
print(merged_df)

print("#"*40, end="\n\n")
#############################

print("Creating Json File")
print("-"*20)
# -----------

merged_df.to_json("df_report_1.json")
print("Created 'df_report.json', Please check")

r = merged_df.T # Rotate
r.to_json("df_report_2.json")


print("""
Created 2 json files,
df_report_1.json
df_report_2.json
please check
""")

print("#"*40, end="\n\n")
#############################
