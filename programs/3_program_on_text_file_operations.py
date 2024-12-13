"""
Get data from web_server.log file
then extract info
then write extracted info to log_report.txt
"""

print("Get data from web_server.log file")
print("-"*20)
# -----------

# Step-1: Connect to file
# -----------
# Absolute path
# my_log_file_handle = open(r"C:\python_training\log\web_server.log", "r")
# Relative Path
my_log_file_handle = open(r"../log/web_server.log", "rb")
# rb-> r-> read only b -> binary file

# Step-2: Read log file content
# -----------
log_file_content = my_log_file_handle.readlines()
print(log_file_content)

# Step-3: Disconnect
# -----------
my_log_file_handle.close()

print("#"*40, end="\n\n")
#############################

print("Checking type of one value")
print("-"*20)
# -----------

print(type(log_file_content[0]))

print("#"*40, end="\n\n")
#############################


print("Extract IP, PICS and printing")
print("-"*20)
# -----------
# log_file_content -> list of bytes
for each_line in log_file_content:
    # each_line -> bytes
    if each_line.startswith(b"123"): # b -> bytes
        sp = each_line.split(b" ") # b -> bytes
        print("sp:", sp, end="\n\n")
        ip = sp[0]
        ip = ip.decode()  # convert to string

        raw_img = sp[6] # '/pics/wpaper.gif'
        # if raw_img.endswith(".jpg") or raw_img.endswith(".gif")
        # OR
        if raw_img.startswith(b"/pics/"):
            img = raw_img.removeprefix(b"/pics/")
            # OR
            img = raw_img[6:] # index-6 to end
            img = img.decode()
        else:
            img = "No Image"

        print(ip, img)


print("#"*40, end="\n\n")
#############################

print("Write to log_report.txt file")
print("-"*20)
# -----------

# my_out_file_handle = open(r"C:\python_training\log\log_report.txt", "w")
# OR
my_out_file_handle = open(r"../log/log_report.txt", "w")

# log_file_content -> list of bytes
for each_line in log_file_content:
    # each_line -> bytes
    if each_line.startswith(b"123"): # b -> bytes
        sp = each_line.split(b" ") # b -> bytes
        # print("sp:", sp, end="\n\n")
        ip = sp[0]
        ip = ip.decode()  # convert to string

        raw_img = sp[6] # '/pics/wpaper.gif'
        # if raw_img.endswith(".jpg") or raw_img.endswith(".gif")
        # OR
        if raw_img.startswith(b"/pics/"):
            img = raw_img.removeprefix(b"/pics/")
            # OR
            img = raw_img[6:] # index-6 to end
            img = img.decode()
        else:
            img = "No Image"

        print(ip, img, file=my_out_file_handle)

my_out_file_handle.close()

print("Created log_report.txt. Please check")

print("#"*40, end="\n\n")
#############################

# COMMENT
# ---------
# my_out_file_handle = open(r"C:\python_training\log\log_report.txt", "w")
# OR
# my_out_file_handle = open(r"../log/log_report.txt", "w")
#############################