
def longestUniqueSubsttr(str):
    test = ""
    maxLength = -1

    if (len(str) == 0):
        return 0
    elif (len(str) == 1):
        return 1

    for c in list(str):
        print(c)
        current = c
        print(current)

        if (current in test):
            test = test[test.index(current) + 1:]
            print(test)
        test = test + c
        print(test)
        maxLength = max(len(test), maxLength)
        print(maxLength)
        print("-------------------")
    return maxLength

string = "pwwkew"
print("The input string is", string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character substring is", length)
