
def Pattern():
    print("please enter row:")
    No = int(input())
    
    print("please enter col:")
    No1 = int(input())
    
    for i in range(0,No):
        for j in range(0,No1):
            print("*",end=" ")
        print()
            
    
if __name__ == "__main__":
    Pattern()