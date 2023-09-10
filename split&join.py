def split_and_join(line):
    line = line.split(' ')       # split will break text with whatever value given in () and convert string into list
    print(line)
    line = '-'.join(line)        # join will join elements in list by given joined eg : '-'
    return line

if __name__ == '__main__':
    line = input("string:")
    result = split_and_join(line)
    print(result)