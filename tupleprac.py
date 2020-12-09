T1=(2,4,6,7,92,22,22,33,44)
T2=(3,8,9,100,222,1223,455)

print(id(T1))
print(id(T2))

print(T1)
print(T2)

tup1 = ("JavaTpoint")  
print(type(tup1))  
#Creating a tuple with single element   
tup2 = ("JavaTpoint",)  
print(type(tup2))

tuple1 = tuple(input("Enter the tuple elements ..."))  
print(tuple1)    
count = 0    
for i in tuple1:    
      print("tuple1[%d] = %s"%(count, i))   
      count = count+1  

#del T1[0]          #error imutable

T1=(3,2,1,1,3,333,23,34)

print(T1)
print(id(T1))

print(T1+T2)

print(T1*2)

print(333 in T1)
print(100 in T1)
print(len(T1))




