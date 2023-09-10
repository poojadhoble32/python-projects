def Find(Val):
    
    if Val%2 == 0:
        print("Number is even")
    else:
        print("number is odd")

def EvenOdd():
    
    print("Please enter number to find out EVEN /Odd number :")
    
    No = int(input())
    
    Find(No)

if __name__ == "__main__":
    EvenOdd()