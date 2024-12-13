"""
Write class for log process activity

Requirement:
l1 = LogProcessClass(r"../log/web_server.log")
ips_list = l1.get_all_ips() # [ip1, ip2, ip3]
all_data = l1.get_all() # [(ip1,img1),(ip2,img2),(ip3,img3),]
l1.to_text_file("my_out_file.txt")
l1.to_json_file("my_out_file.json")
"""

print("Class for log process activity")
print("-"*20)
# -----------

class LogProcessClass:
    def __init__(self, log_file_path):
        """
        Read log file content and keep it in variable
        :param log_file_path:
        """
        # Read the log file
        # -----------
        my_log_file_handle = open(log_file_path, "rb")
        self.log_file_content = my_log_file_handle.readlines()
        my_log_file_handle.close()
        # -----------

    def get_all_ips(self):
        output_list = []
        for each_line in self.log_file_content:
            # each_line -> bytes
            if each_line.startswith(b"123"):  # b -> bytes
                sp = each_line.split(b" ")  # b -> bytes
                # print("sp:", sp, end="\n\n")
                ip = sp[0]
                ip = ip.decode()  # convert to string
                output_list.append(ip)
        return output_list

    def get_all(self):
        output_dictionary = {}
        my_key = 0
        for each_line in self.log_file_content:
            # each_line -> bytes
            if each_line.startswith(b"123"):  # b -> bytes
                sp = each_line.split(b" ")  # b -> bytes
                # print("sp:", sp, end="\n\n")
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

    def write_to_text_file(self, text_file_path):
        my_text_file_handle = open(text_file_path, "w")

        # output_dictionary = {0:(ip, img), 1:(ip, img)}
        # output_dictionary.values() = [(ip, img), (ip, img)]
        output_dictionary = self.get_all()
        for i, j in output_dictionary.values():
            print(i, j, sep="\t", file=my_text_file_handle)
        my_text_file_handle.close()


    def write_to_json_file(self, json_file_path):
        my_json_file_handle = open(json_file_path, "w")
        # output_dictionary = {0:(ip, img), 1:(ip, img)}
        output_dictionary = self.get_all()
        import json
        json.dump(output_dictionary, my_json_file_handle)
        my_json_file_handle.close()


print("#"*40, end="\n\n")
#############################

print("Using LogProcess Class")
print("-"*20)
# -----------

l1 = LogProcessClass(r"../log/web_server.log")

ips_list = l1.get_all_ips()
print("ips_list:", ips_list, sep="\n", end="\n\n")

all_data_in_dictionary = l1.get_all()
print("all_data_in_dictionary:", all_data_in_dictionary, sep="\n", end="\n\n")

l1.write_to_text_file("log_process_class_report.txt")
print("Created log_process_class_report.txt please check", sep="\n", end="\n\n")

l1.write_to_json_file("log_process_class_report.json")
print("Created log_process_class_report.json please check", sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#############################
