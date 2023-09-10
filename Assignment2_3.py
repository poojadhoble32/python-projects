def factorial():
    print("enter number to check factorial:")
    No = int(input())
    ans = 1
    
    for i in range(No,0,-1):
        ans = i * ans
        
    print("factorial of",No,"is :",ans)

if __name__ == '__main__':
    factorial()