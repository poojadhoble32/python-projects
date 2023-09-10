from functools import reduce

def AcceptList():
    L = []
    print("please enter size:")
    
    size = int(input())
    
    print("enter numbers in list:")
    
    for i in range(0,size):
    
        L.append(int(input()))
        
    F = list(filter(lambda x : x%2!=0,L))
    
    print("Prime numbers after filtered:",F)
    
    M = list(map(lambda x : x*2,F))
    
    print("updated list after multiply by 2 of each filtered number:",M)
    
    R = reduce(lambda x,y : x if x>y else y,M)
    
    print("Max of all list numbers after filter and mapping:",R)

if __name__ == "__main__":
    AcceptList()