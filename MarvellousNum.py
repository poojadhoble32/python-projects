def ChkPrime(L):
    sum = 0
    for i in range(0,len(L)):
        if L[i]%2 != 0:
            sum = sum + L[i]
            
    return sum