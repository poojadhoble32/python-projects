def Pattern():
    print("please enter row:")
    No = int(input())
    
    print("please enter col:")
    No1 = int(input())
    
    for i in range(1,No+1):
        for j in range(No1,0,-1):
            if i<=j:
                print(i,j,"*",end="     ")
                
            if i>j:
                break
        print()
            
    
if __name__ == "__main__":
    Pattern()