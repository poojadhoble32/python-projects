from string import ascii_letters           # ascii_letters contains a-Z alphabets and difference between a & A is 27

s = "abcdezz34#%&"
s1 = ''

for i in range(0,len(s),2):
    if s[i] in ascii_letters:
        s1 = s1+ascii_letters[ascii_letters.index(s[i])+1]  # The Python upper() method is used to convert lowercase letters in a string to uppercase. The isupper() method, on the other hand, returns True if all the letters in a string are uppercase.
    elif (i<=9 and i>=0):
        s1 = s1+'@'
    else:
        s1 = s1+'7'

print(s1.upper())
