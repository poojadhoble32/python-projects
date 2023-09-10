
class demo:
    
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B
        
    def add(self):
        ans = self.no1 + self.no2
        return ans
        
    def sub(self):
        ans = self.no1 - self.no2
        return ans

def main():
    print("inside main method")
    
    obj = demo(11,10)
    
    output = obj.add()
    print("addition is :",output)
    
    output = obj.sub()
    print("subtraction is :",output) 
    
    objx = demo(21,10)
    
    output = objx.add()
    print("addition is :",output)
    
    output = objx.sub()
    print("subtraction is :",output) 

if __name__ == "__main__":
    main()