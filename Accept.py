import os
import Find


class Accept:

    path = "Demo"
    ext1 = ".txt"
    ext2 = ".doc"

    try:
        flag = os.path.isabs(path)

        if flag == False:
            path = os.path.abspath(path)

        if os.path.exists(path):
            obj = Find.Find(path, ext1, ext2)
            obj.run()
        else:
            raise Exception("Invalid path")

    except Exception as e:
        print(e)
