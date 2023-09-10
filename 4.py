import threading 
import time

def small(str1):
    
    S = [char for char in str1 if char.islower()]
    
    print(S)

def capital(str2):

    S1 = [char1 for char1 in str2 if char1.isupper()]
    
    print(S1)

def digits(str3):

    S3 = [char2 for char2 in str3 if char2.isdigit()]
    
    print(S3)

def accept():
    
    strs = "AlcoHoLe123SiX10"

    T1 = threading.Thread(target = small, args = (strs,))
    T2 = threading.Thread(target = capital, args = (strs,))
    T3 = threading.Thread(target = digits, args = (strs,))
    
    T1.start()
    T2.start()
    T3.start()
    
    T1.join()
    T2.join()
    T3.join()
    
if __name__ == "__main__":
    start_time = time.process_time()
    accept()
    end_time = time.process_time()
    print("execution time : ",start_time - end_time)