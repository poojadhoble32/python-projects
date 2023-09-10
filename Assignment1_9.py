def EvenNum():
    print("First 10 even numbers are :")
    
    count = 0
    
    for i in range(1,30):
        
        if i%2 == 0:
            print(i,end="  ")
            count+=1
            
        if count == 10:
            break

if __name__ == "__main__":
    EvenNum()