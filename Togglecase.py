s = input("enter the string:")
s1 = ''

for i in s:
    if i.islower():
        s1 = s1+i.upper()
    elif i.isupper():
        s1 = s1+i.lower()
    else:
        s1 = s1+'?'

print(s1)
