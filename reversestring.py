s = "bGHsff334$%d"
s1 = ''

for i in range(len(s)-1,-1,-1):          # len count from 1 and range run from 0-4 for 5 but len is 5
    if s[i].islower():
        s1 = s1 + s[i].upper()
    elif s[i].isupper():
        s1 = s1 + s[i].lower()
    else:
        s1 = s1 + '?'

print(s1)        # str() to convert into string