"""
Program on capturing logs
"""

print("Configuring logger")
print("-"*20)
# -----------

import logging

my_logger = logging.getLogger(__name__)

logging.basicConfig(filename="my_captured_log.log",
                                filemode="w",
                                level=logging.DEBUG,
                                format="%(levelname)s : %(asctime)s : %(filename)s : %(message)s"
                                )

print("#"*40, end="\n\n")
#############################

print("Testing Configured Logger")
print("-"*20)
# -----------

my_logger.info("This is INFO")
my_logger.debug("This is DEBUG")
my_logger.warning("This is WARNING")
my_logger.critical("This is CRITICAL")
my_logger.error("This is ERROR")


print("Log captured in 'my_captured_log.log', Please check")

print("#"*40, end="\n\n")
#############################

print("Using logging in our code")
print("-"*20)
# -----------

my_logger.info("Log file reading started..")

try:
    my_logger.info("Entered try block")

    my_logger.info("Opening file for reading")
    my_file_handle = open("D:/sdsafsadsad.txt", "r")
    my_logger.info("File open success")

    my_logger.info("Reading file content")
    file_content = my_file_handle.read()
    my_logger.info("Reading file content success")

    my_logger.info("Closing File handle")
    my_file_handle.close()
    my_logger.info("Closing File handle completed")

except Exception as e:
    my_logger.error(f"Not able to complete file read operations: Reason is:{e}")
    my_logger.info("Stopping program execution here")
    print("Log captured in 'my_captured_log.log', Please check")
    exit()

my_logger.info("Log file reading operations completed")

print("Log captured in 'my_captured_log.log', Please check")

print("#"*40, end="\n\n")
#############################
