L1=[200,100,300,500,400]
L2=[200,300,600,700,800]

for i in L1:
    for j in L2:
        if i==j:
            L2.remove(j)

print(L2)
L3=L1+L2
print(L3)

