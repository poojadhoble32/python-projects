L1=[1,2,3,4]
L2=[3,5,4,6,6]
L3=[]

for i in L1:
    for j in L2:
        if i==j:
            L3=L3+[i]

print(L3)
