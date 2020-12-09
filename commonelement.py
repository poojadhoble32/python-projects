L1=[10,20,30,40]
L2=[40,50,10,20]
L3=0

for i in L1:
    for j in L2:
        if i==j:
            L3=L3+i

print(L3)
