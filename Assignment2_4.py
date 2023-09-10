def FactAdd():
    print("enter number to check factors Add:")
    No = int(input())
    ans = 0
    
    for i in range(1,int(No/2)+1):
        if No%i == 0:
            ans = i + ans
        
    print("factors addition of",No,"is :",ans)

if __name__ == '__main__':
    FactAdd()