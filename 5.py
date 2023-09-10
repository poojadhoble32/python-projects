import time
import threading 

def numberlist(no):
    
    print("1 to 50 numbers are : ")
    
    for i in range(1,no+1):
        print(i)
    
def revlist(no):

    print("50 to 1 numbers are : ")
    
    for i in range(no,0,-1):
        print(i)
            
def accept():

    num = 50
    
    T1 = threading.Thread(target = numberlist, args = (num,))
    T2 = threading.Thread(target = revlist, args = (num,))
    
    T1.start()
    T1.join()
    
    T2.start()
    T2.join()
    
    print("exit from main")

if __name__ == "__main__":
    start_time = time.process_time()
    accept()
    end_time = time.process_time()
    print("total execution time is : ",start_time - end_time)