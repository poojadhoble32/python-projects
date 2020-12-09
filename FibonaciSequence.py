T1=0
T2=1

def Fibonaci(T1,T2):
    print(T1)
    print(T2)
    for i in range(9):
        T3=T1+T2
        print(T3)
        T1=T2
        T2=T3

Fibonaci(T1,T2)

