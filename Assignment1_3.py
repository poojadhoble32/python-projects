def Result(v1,v2):
    Ans = v1+v2
    
    return Ans

def Add():
    print("Please enter first number :")
    no1 = int(input())
    
    print("Please enter second number :")
    no2 = int(input())
    
    Ret = Result(no1,no2)
    
    print("Addition of two numbers is :",Ret)
    
if __name__ == "__main__":
    Add()