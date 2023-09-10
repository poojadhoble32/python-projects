def main():
    print("Enter number :")
    No = int(input())
    
    print("Factors are : ")
    
    for i in range(1,No):
        if No%i==0:
            print(i)

if __name__=="__main__":
    main()