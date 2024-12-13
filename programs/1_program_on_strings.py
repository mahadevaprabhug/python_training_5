"""
from the given string, extract
IP
DATE
PICS
URL

Expected Output
-----------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
-----------------
"""

print("input data:")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
#############################


print("type of input data:")
print("-"*20)
# -----------

print(type(input_data))

print("#"*40, end="\n\n")
#############################

print("Extract IP: 1 - WAY: PARTIAL")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
#############################

print("Extract IP: 2 - WAY")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_1st_space = input_data.index(" ")

ip = input_data[0:index_of_1st_space]
print(ip)

# Example:
# >>> # About 'index' method
# >>> # feature-1
# >>> my_string = "WEL COME"
# >>> my_string.index("E") # returns index of 1st occurance
# 1
# >>> # feature-2
# >>> my_string = "WEL COME"
# >>> my_string.index("E", 3) # start looking from index-3
# 7
# >>> # feature-3
# >>> my_string = "WEL COME"
# >>> my_string.index("COME") # returns index of C
# 4

print("#"*40, end="\n\n")
#############################

print("Extract IP: 3 - WAY")
print("-"*20)
# -----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split(" ")
print("sp:", sp, end="\n\n")

ip = sp[0]
print(ip)

print("#"*40, end="\n\n")
#############################
