class arithmetic:
    S = []
    sum = 0
    
    def __init__(self,value):
        self.value = value
        
    def ChkPrime(self):
        if self.value%2 != 0:
            return True
        else :
            return False
    
    def ChkPerfect(self):
        if arithmetic.sum == self.value:
            return True
        else:
            return False
    
    def Factors(self):
        
        for i in range(1,int(self.value/2)+1):
            if self.value%i == 0:
                arithmetic.S.append(i)
                
        print("Factors of {} are: {}".format(self.value,arithmetic.S))
    
    def SumFactors(self):
        for i in range(0,len(arithmetic.S)):
            arithmetic.sum = arithmetic.sum + arithmetic.S[i]
            
        return arithmetic.sum
    
    
def accept():
    print("enter value:")
    value = int(input())
    
    obj = arithmetic(value)
    
    ret=obj.ChkPrime()
    if ret == True:
        print("{} is not prime".format(value))
    else:
        print("{} is prime".format(value))
        
    obj.Factors()
    
    ret1 = obj.SumFactors()
    print("sum of factors of {} is : {}".format(value,ret1))
    
    ret2 = obj.ChkPerfect()
    if ret2 == True:
        print("{} is perfect number".format(value))
    else:
        print("{} is not perfect number".format(value))
    
    
if __name__ == "__main__":
    accept()
    