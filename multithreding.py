'''
from threading import *
print(current_thread().getName())
def mt():
    print("child thread")
child=Thread(target=mt)
child.start()
print("executing thread name :",current_thread().getName())
'''
from threading import *
import threading
import time
class mythread(threading.Thread):
    def run(self):
        for x in range(7):
            print("hi from child")

a=mythread()
a.start()
a.join()
print("bye from",current_thread().getName())
