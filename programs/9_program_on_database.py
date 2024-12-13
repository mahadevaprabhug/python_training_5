"""
Get data from web_server.log file
then
extract using regular expression
then
Send to database
"""

"""
How to communicate with SQL/No-SQL database in python?

python-program  <--Using Library-->  Any Databases (SQL/No-SQL)

Example:
python-program  <--Using Library(cx-oracle)-->  Oracle Databases
python-program  <--Using Library(mysql.connector)-->  MySQL Databases
python-program  <--Using Library(sqlite3)-->  SQLite Databases
"""

"""
We need ONE database.
- We can use SQLite database
- SQLite database is lightweight database
- SQLite database will not run any database server like other database will run server
    like oracle db server
- SQLite database will just create one file, on that file we can run SQL query
"""

"""
How to create or communicate with SQLite database?
2 OPTIONS
OPTION-1: Using SQLite database software
OPTION-2: WITHOUT Using SQLite database software,
            Using python library sqlite3, we can create or communicate with SQLite database
"""

print("Create or connect to database 'my_database.sqlite3'")
print("-"*20)
# -----------

import sqlite3

print("Creating or connect to database 'my_database.sqlite3'")
# my_db_connection = sqlite3.connect(r"C:\python_training\programs\my_database.sqlite3")
# OR
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("Done\n")

print("Creating cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Creating table if table is not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")

print("#"*40, end="\n\n")
#############################

print("Get data from web_server.log file")
print("-"*20)
# -----------

my_log_file_handle = open(r"../log/web_server.log", "rb")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()
print(log_file_content)

print("#"*40, end="\n\n")
#############################

print("Extract IP, DATE, PICS, URL")
print("-"*20)
# -----------

import re

for each_line in log_file_content:

    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|DELETE|PATCH)\s/(pics/(\w+\.(gif|jpg)))?.*HTTP.*(http[s]?://[a-z./A-Z_0-9]+).*',each_line)

    if match_result is not None:
        ip = match_result.group(1)
        ip = ip.decode() # convert to string
        dt = match_result.group(2)
        dt = dt.decode()
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        else:
            img = img.decode()
        url = match_result.group(7)
        url = url.decode()
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{dt}', '{img}', '{url}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records are inserted\n")

print("#"*40, end="\n\n")
#############################

print("Executing Select Query")
print("-"*20)
# -----------

my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
my_db_result = my_db_cursor.fetchall()
print(my_db_result)
my_db_connection.close()

print("#"*40, end="\n\n")
#############################
