import psutil
import os
import time
from sys import *

def ProcessDisplay(log_dir = "Marvellous"):
    listprocess = []
    
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    print("1")        
    seperator = "-"*80
    log_path = os.path.join(log_dir,"Marvellouslog.log")
    print(log_path)
    f = open(log_path, 'w')
    f.write(seperator+"\n")
    f.write("Marvellous Infosystems Process Logger :"+time.ctime()+"\n")
    f.write(seperator+"\n")
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])       # converted data to dict
            pinfo['vms'] = proc.memory_info().vms / (1024*1024)
            
            listprocess.append(pinfo);
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    
    for element in listprocess:
        f.write(str(element))      #file accepts only string & data type of element is dict which file will not accept so convert it into str
        f.write("\n")
    
def main():

    print("Marvellous Infosystems : Python Automation & ML")

    print("Application name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This script is used to add log record of running processes")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
    
    except ValueError:
        print("Error : Invalid datatype of input")
        
    except Exception:
        print("Error : Invalid input")
        
if __name__ == "__main__":
    main()