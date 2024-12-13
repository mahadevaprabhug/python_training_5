"""
Requirement: Write a function for processing log file
1. one argument i.e log_file_path
2. return extracted data in dictionary
    like {0:(ip, img), 1:(ip, img)}
"""

print("Log file process function")
print("-"*20)
# -----------


def log_process_function(log_file_path):
    """
    This function will read log file, then extract info then
    it will return extracted info in dictionary
    :param log_file_path:
    :return output_dictionary:
    """
    # Read the log file
    # -----------
    my_log_file_handle = open(log_file_path, "rb")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    # -----------

    # Extract Info and return
    # -----------
    # output_dictionary = {0:(ip, img), 1:(ip, img)}
    output_dictionary = {}
    my_key = 0
    for each_line in log_file_content:
        # each_line -> bytes
        if each_line.startswith(b"123"):  # b -> bytes
            sp = each_line.split(b" ")  # b -> bytes
            print("sp:", sp, end="\n\n")
            ip = sp[0]
            ip = ip.decode()  # convert to string

            raw_img = sp[6]  # '/pics/wpaper.gif'
            # if raw_img.endswith(".jpg") or raw_img.endswith(".gif")
            # OR
            if raw_img.startswith(b"/pics/"):
                img = raw_img.removeprefix(b"/pics/")
                # OR
                img = raw_img[6:]  # index-6 to end
                img = img.decode()
            else:
                img = "No Image"

            each_line_tuple = (ip, img)
            output_dictionary[my_key] = each_line_tuple
            my_key += 1
    return output_dictionary

print("#"*40, end="\n\n")
#############################

print("Calling function")
print("-"*20)
# -----------

func_1_result = log_process_function(log_file_path=r"../log/web_server.log")
print("func_1_result:", func_1_result)

print("#"*40, end="\n\n")
#############################

