
L1 = ["John", 102, "USA",23.2,34,'pooja','xyz',80]    
L2 = [1, 2, 3, 4, 5, 6,6,2,3,8]   

print(type(L1))
print(type(L2))    #type of data

print(L1)          #print elements of list
print(L2)

print(id(L1))      #id means address of list
print(id(L2))

print(L1==L2)      #compare both list elements.elements from the list must have same index then only return true

print("name : %s\t id : %d\tper : %f"%(L1[0],L1[1],L1[3]))   #access elements 

print(L2[0],L2[1],L2[2])         #acess elements by index

print(L1[1:4])               #split or sublist or slice

print(L1[:])                    #whole list will take

print(L1[0:])                 

print(L1[:7])                

print(L1[0:7:2])             #elements in 2 steps

print(L1[-1],L1[-3])

print(L1[0:-4])

print(L1[-6:-1])

print(L1[-1:-4])

L2.reverse()                #reverse list using reverse method
print(L2)

print(L1[::-1])                #reverse using slicing optr

y=range(6)                      #range func working as list range start with 0
for x in y:
    print(x)

print(type(y))

print(id(L1))

del L1[2]

print(L1)

print(id(L1))

L1=[3,4,5,6,7,78]

print(id(L1))

print(L1)




