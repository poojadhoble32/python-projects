def Output():
    print("Please enter number to print pattern :")
    
    no = int(input())
    i=1
    
    while(i<=no):
        print("*",end="  ")
        i+=1
        
if __name__ == "__main__":
    Output()