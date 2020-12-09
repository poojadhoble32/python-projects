def EvenAdd(L):
    i=0;sum=0
    
    if L%2==0:
        sum=sum+L
        L--

    return EvenAdd(L)
    return sum    
        
print(EvenAdd(10))
