def Find():
    print("please enter number to check if it is divisible by 5 :")
    
    no = int(input())
    
    if no%5 == 0:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    Find()