Num=int(input("enter the number:"))
Ret=False

def perfect(Num):
    sum1=0
    for i in range(1,Num):
        if(Num%i==0):
            sum1=sum1+i

    if sum1==Num:
        return True


Ret=perfect(Num)

if Ret==True:
    print(f"The given number {Num} is perfect number")
else:
     print(f"The given number {Num} is not perfect number")
