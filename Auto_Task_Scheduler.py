import schedule
import time
import datetime

def fun_Minute():
    print("Current time is")
    print(datetime.datetime.now())
    print("scheduler executed after minute")
    
def fun_Hour():
    print("current time is")
    print(datetime.datetime.now())
    print("scheduler executed after hour")
    
def fun_Day():
    print("current time is")
    print(datetime.datetime.now())
    print("scheduler executed after day")
    
def fun_Afternoon():
    print("current time is")
    print(datetime.datetime.now())
    print("scheduler executed at 12")
    
def main():
    print(" Marvellous Infosystem ")
    
    print("Python job schedular")
    print(datetime.datetime.now())
    
    schedule.every(1).minutes.do(fun_Minute)
    
    schedule.every().hour.do(fun_Hour)
    
    schedule.every().day.at("13:21").do(fun_Afternoon)
    
    schedule.every().sunday.do(fun_Day)
    
    schedule.every().wednesday.at("13:20").do(fun_Day)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()