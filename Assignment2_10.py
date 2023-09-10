def Digit():
    print("enter number:")
    No = int(input())
    Add=0
    D=0
    
    while(No!=0):
        No=No/10
        D=No%10
        
        Add=Add+D
        
    print("Addition of digits is:",int(Add))
       

if __name__ == '__main__':
    Digit()