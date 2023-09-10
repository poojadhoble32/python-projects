
class numbers:
    def __init__(self):
        self.size = 0
        self.arr = list()
        
    def accept(self):
        print("enter how many elements you want:")
        self.size = int(input())
        
        print("please enter theelements")
        value = 0
        for i in range(0,self.size):
            value = int(input())
            self.arr.append(value)
            
    def display(self):
        print("elements from list are:")
        for i in range(0,self.size):
            print(self.arr[i])
            
    def summation(self):
        sum = 0
        for i in range(0,self.size):
            sum = sum + self.arr[i]
        return sum

def main():
    obj = numbers()
    obj.accept()
    obj.display()
    
    output = obj.summation()
    print("summation is:",output)

if __name__ == "__main__":
    main()