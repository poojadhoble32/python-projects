# find kth smallest element

import array as arr

a = arr.array('i', (4,9,8,7,0,1,3,2))
k = 4

for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[j] > a[i]:
            a[j],a[i] = a[i],a[j]

print(a)
print(a[k-1])