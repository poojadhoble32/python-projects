set1={9,8,74,3,7,8}   #element repeatation not allowed

print(set1)
print(id(set1))

set1={4,3,2,1}
print(set1)
print(id(set1))

Frozenset = frozenset([9,1,2,3,4,5])     #frozenset cant change values
print(type(Frozenset))    
print("\nprinting the content of frozen set...")    
for i in Frozenset:
    print(i);    
Frozenset.add(6)
