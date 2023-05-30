from threading import*
from time import *

def print_time (thread_name, delay):
    count = 0
    while count < 3:
        sleep(delay)
        count +=1
        print(thread_name,"------> ", ctime())

thread1 = Thread(target=print_time, args=("Thread_1", 1))
thread2 = Thread(target=print_time, args=("Thread_2", 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done.....")    