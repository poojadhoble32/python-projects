from functools import reduce

def AcceptList():
    L = []
    print("please enter size:")
    
    size = int(input())
    
    print("enter numbers in list:")
    
    for i in range(0,size):
    
        L.append(int(input()))
        
    F = list(filter(lambda x : x%2==0,L))
    
    print("Even numbers after filtered:",F)
    
    M = list(map(lambda x : x*x,F))
    
    print("updated list after finding square of each filtered number:",M)
    
    R = reduce(lambda x,y : x+y,M)
    
    print("addition of all list numbers after filter and mapping:",R)

if __name__ == "__main__":
    AcceptList()