L=[23,45,88,23,56,78,96]
SecLarge=0

Large=L[0]

for i in L:
    if(i>Large):
        SecLarge=Large
        Large=i

print(SecLarge)
