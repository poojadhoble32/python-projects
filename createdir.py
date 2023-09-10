import os
import pathlib
import shutil


class createdir:

    def __init__(self, dir1, dir2, ext):
        self.dir1 = dir1
        self.dir2 = dir2
        self.ext = ext


    def CopyFilesTo(self):


        for folder, subfolder, filename in os.walk(self.dir1):

            for self.file in filename:
                self.ext1 = pathlib.Path(self.file).suffix

                if self.ext1 == self.ext:
                    newfilepath = os.path.join(self.dir2, self.file)

                    oldfilepath = os.path.join(self.dir1, self.file)

                    shutil.copyfile(oldfilepath, newfilepath)


    def run(self):
        if not os.path.exists(self.dir2):
            os.makedirs(self.dir2)
        else:
            print("%s is already exist"%self.dir2)

        flag = os.path.isabs(self.dir2)

        if flag == False:
            self.dir2 = os.path.abspath(self.dir2)

        self.CopyFilesTo()
