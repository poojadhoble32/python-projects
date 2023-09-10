print("Print * pattern")

for i in range(0,5):
    for j in range(0,i+1):
        if i >= j:
            print("*  ",end='')
        else:
            break
    print()