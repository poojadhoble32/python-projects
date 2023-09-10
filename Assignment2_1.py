import Arithmetic

def function():
    ans = 0
    
    print("enter 1st number:")
    no=int(input())
    
    print("enter 2nd number:")
    no1=int(input())
    
    ans=Arithmetic.add(no,no1)
    print("addition is:",ans)
    
    ans=Arithmetic.sub(no,no1)
    print("substraction is:",ans)
    
    ans=Arithmetic.mult(no,no1)
    print("Mult is:",ans)
    
    ans=Arithmetic.div(no,no1)
    print("Div is:",ans)
    

if __name__ == "__main__":
    function()