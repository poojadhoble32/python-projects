def outer(a,b):
    def inner():
        c=a+b
        return c

    ans=inner()
    return ans+5

ret=outer(4,10)
print(f"addition is:{ret}")
    
