#An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).

#import numpy as np
#arr = np.array([1, 2, 3])  #array using numpy
import array as arr

a = arr.array('i',(8,9,6,4,2))            #for float num use 'd' , append() increase size by one for multiple added elments while extend increase len as per no. of elemtns aded

b = a[0]

for i in range(1,len(a)):
    if a[i]>b:
        b = a[i]

print("max is {}".format(b))
