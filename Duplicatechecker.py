import hashlib
import os.path
import time


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
    fd = open("Duplicate.log", 'w')
    dup = {}

    try:
        flag = os.path.isabs(dirname)

        if flag == False:
            dirname = os.path.abspath(dirname)

        if os.path.exists(dirname):
            for folder, subfolder, files in os.walk(dirname):

                for filename in files:
                    path = os.path.join(folder, filename)
                    checksumvalue = checkchecksum(path)

                    if checksumvalue not in dup:
                        dup[checksumvalue] = path
                    else:
                        fd.write("{} : {} \n".format(checksumvalue, path))
                        os.remove(path)

            print(dup)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    starttime = time.process_time()
    accept()
    endtime = time.process_time()
    total = endtime - starttime
    print("script process time is {}".format(total))