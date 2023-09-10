import time
import threading 

def even(no):
    
    cnt = 0
    
    print("Even numbers are :")
    
    for i in range(1,no):
        if (i%2 == 0) and (cnt < 10):
            print(i,end = " ")
            cnt += 1
    
def odd(no):

    cnt = 0
    
    print("odd numbers are : ")
    
    for i in range(1,no):
        if (i%2 != 0) and (cnt < 10):
            print(i,end = " ")
            cnt += 1

def accept():

    num = 30
    
    T1 = threading.Thread(target = even, args = (num,))
    T2 = threading.Thread(target = odd, args = (num,))
    
    T1.start()
    T2.start()
 
    T1.join()
    T2.join()

if __name__ == "__main__":
    start_time = time.process_time()
    accept()
    end_time = time.process_time()
    print("total execution time is : ",start_time - end_time)