T1=0
T2=1
print(T1)
print(T2)
count=10

def Fibonaci(T1,T2, count):
        T3=T1+T2
        print(T3)
        T1=T2
        T2=T3
       
        if(count>=1):
            count-=1
            Fibonaci(T1,T2,count)

Fibonaci(T1,T2,count)
