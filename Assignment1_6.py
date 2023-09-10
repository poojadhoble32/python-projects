def Find():
    print("Please enter number to check +/-/0 :")
    
    no = int(input())
    
    if no < 0:
        print("number is -ve")
    elif no > 0:
        print("number is +ve")
    else:
        print("number is Zero")

if __name__ == "__main__":
    Find()