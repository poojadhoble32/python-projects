def Prime():
    print("enter number to check it is prime or not:")
    No = int(input())
    
    if No%2 != 0:
        print("Number is prime")
    else:
        print("Number is not prime")
       

if __name__ == '__main__':
    Prime()