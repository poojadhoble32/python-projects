#Count pairs with given sum

import array as arr

#a = arr.array('i', (4,9,8,7,0,1,3,2))
a = arr.array('i', (2,1,2,1,0,0,0,2) )    # convert lst into array : res = array("i", test_list)
sum = 3

for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[j] + a[i] == sum:
            print('(',a[i],a[j],')')

