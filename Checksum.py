'''
import hashlib

# encoding GeeksforGeeks using md5 hash
# function
text = 'GeeksforGeeks'
result = hashlib.md5(text.encode())            #convert string into byte

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result)    #converted in byte
print(result.digest())               #converted encoded data in byte
print(result.hexdigest())       # returns encoded in hexadecimal
'''

import hashlib
import os.path


def checkchecksum(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()

    return hasher.hexdigest()

def accept():
    dirname = 'Demo'

    try:
        flag = os.path.isabs(dirname)

        if flag == False:
            dirname = os.path.abspath(dirname)

        if os.path.exists(dirname):
            for folder, subfolder, files in os.walk(dirname):

                for filename in files:
                    path = os.path.join(folder, filename)
                    checksumvalue = checkchecksum(path)
                    print("Checksum of {} is {}".format(filename, checksumvalue))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    accept()