"""
multithreading:
"""

print("WITHOUT Using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]

my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
#############################

print("Using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]

from threading import Thread

# Creating 2 threads
my_thread_1 = Thread(target=my_square_function, args=(L,))
my_thread_2 = Thread(target=my_cube_function, args=(L,))

# Start both the threads
my_thread_1.start()
# It will just start the thread and proceed to next line,
# Which means, it will not wait for that thread to complete
my_thread_2.start()


# Make both threads wait here, till it completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
#############################

print("WITH DELAY: WITHOUT Using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
#############################

print("WITH DELAY: Using multithreading")
print("-"*20)
# -----------

import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

from threading import Thread

# Creating 2 threads
my_thread_1 = Thread(target=my_square_function, args=(L,))
my_thread_2 = Thread(target=my_cube_function, args=(L,))

# Start both the threads
my_thread_1.start()
# It will just start the thread and proceed to next line,
# Which means, it will not wait for that thread to complete
my_thread_2.start()


# Make both threads wait here, till it completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
#############################
