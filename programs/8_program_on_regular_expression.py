"""
Get data from web_server.log file
then extract using regular expression
"""
print("Get data from web_server.log file")
print("-"*20)
# -----------

my_log_file_handle = open(r"../log/web_server.log", "rb")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()
print(log_file_content)

print("#"*40, end="\n\n")
#############################

print("Check whether it is IP address line or not")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    # match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]',each_line)
    # OR
    match_result = re.match(br'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    # br -> b -> bytes -> r-> raw string
    print("each_line:", each_line)
    print("match_result:", match_result, end="\n\n")

# COMMENT
r"""
Regular Expression

IDENTIFIERS
---------------
\d -> to tell ANY ONE digit b/n 0 to 9
\D -> to tell ANY ONE non-digit. Except 0 to 9, any character
. -> to tell any ONE any character
\. -> strictly ONE DOT
[0-9] -> to tell ANY ONE digit b/n 0 to 9
---------------

QUANTIFIERS
---------------
\d{3} -> \d 3 numbers. i.e \d\d\d
\d{1,3} -> \d{1,3} like (\d|\d\d|\d\d\d)
---------------

MODIFIERS
---------------
* -> makes 0 or more times
+ -> makes 1 or more times
? -> makes 0 or one time
---------------

"""

print("#"*40, end="\n\n")
#############################

print("Extract IP")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    # match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]',each_line)
    # OR
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3})(.*)', each_line)
    # br -> b -> bytes -> r-> raw string
    if match_result is not None:
        ip = match_result.group(1)
        ip = ip.decode() # convert to string
        print(ip)
        remaining = match_result.group(2)
        print(remaining)

# COMMENT
r"""
put () to IP address pattern
- This is called group
- each will be having index number starting 1

"""

print("#"*40, end="\n\n")
#############################

print("Extract IP, DATE")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    # match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]',each_line)
    # OR
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4})(.*)', each_line)
    # br -> b -> bytes -> r-> raw string
    if match_result is not None:
        ip = match_result.group(1)
        ip = ip.decode() # convert to string
        dt = match_result.group(2)
        dt = dt.decode()
        print(ip, dt)
        remaining = match_result.group(3)
        print("remaining:", remaining, end="\n\n")

# COMMENT
r"""
26/Apr/2000

26
---
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits

\d{1,2} # Minimum 1, maximum 2 digits
[0-9]{1,2} # Minimum 1, maximum 2 digits
\d?\d # Minimum 1, maximum 2 digits
[0-9]?[0-9] # Minimum 1, maximum 2 digits
\d?[0-9] # Minimum 1, maximum 2 digits
[0-9]?\d # Minimum 1, maximum 2 digits
---

Apr
---
[a-zA-Z][a-zA-Z][a-zA-Z]
OR 
[a-zA-Z]{3}
OR
[A-Z][a-z][a-z]
OR
[A-Z][a-z]{2}
OR
(Jan|Feb|Mar)
---


"""

print("#"*40, end="\n\n")
#############################

print("Extract IP, DATE, PICS")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    # PROVIDED LESS INFORMATION
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(\w+\.[a-z]{3}).*', each_line)

    # PROVIDED MORE INFORMATION
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|DELETE|PATCH)\s/pics/(\w+\.(gif|jpg))\sHTTP.*',each_line)

    # Making (pics/wpaper.gif) OPTIONAL so that lines which are not having
    # image names are also considered
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|DELETE|PATCH)\s/(pics/(\w+\.(gif|jpg)))?.*HTTP.*',each_line)

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
        print(ip, dt, img)
        # remaining = match_result.group(3)
        # print("remaining:", remaining, end="\n\n")

# COMMENT
r"""

\s -> One Space

a2hlogo.jpg

a2hlogo
----
[a-zA-Z_0-9]+
OR
\w+
----

jpg
---
[a-z][a-z][a-z]
OR
[a-z]{3}
OR
(jpg|gif)
---

"""

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
        print(ip, dt, img, url)
        # remaining = match_result.group(3)
        # print("remaining:", remaining, end="\n\n")

# COMMENT
r"""

Sample data is like
8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05

http[s]?://[a-z./A-Z_0-9]+

https? -> Only s is optional
http[s]? -> Only s is optional 
(https)? -> complete https is optional
[https] -> Any one character in this group. 
#           It can be 'h'
# OR
#           It can be 't'
# OR
#           It can be 'p'
# OR
#           It can be 's'

"""

print("#"*40, end="\n\n")
#############################
