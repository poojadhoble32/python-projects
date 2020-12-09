L=[11,23,45,6,7,3,33,11,33,6,100,11,33,33]
D={}

for i in L:
    count=0
    for j in L:
       if(j==i):
          count+=1
    D[i]=count

print("occurance of each element is :",D)
    
