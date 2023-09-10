'''
str = "****** this is string example....wow!!! *********"
print (str.strip('*'))       # strip fun cut from string given in ()
'''
from collections import Counter
import re

def count_substring(s, ss):
    c2 = 0

    #c2 = s.Counter(ss)
    #c2 = len(re.findall(ss, s))
    c2 = len(re.findall('(?=cdc)', s))

    #c2 = s.count(ss)

    return c2


if __name__ == '__main__':
    string = 'abcdcdc'
    sub_string = 'cdc'

    count = count_substring(string, sub_string)
    print(count)