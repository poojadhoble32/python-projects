import os
import pathlib

class findext:
    fd = open("records.log",'w')
    count = 0

    def __init__(self, path, ext):
        self.path = path
        self.ext = ext

    def run(self):
        for folder,subfolder,filename in os.walk(self.path):
            findext.fd.write("folder name is %s : \n"%folder)

            findext.fd.write("\n")

            for sub in subfolder:
                findext.fd.write("subfolder name is %s : \n"%sub)

            findext.fd.write("\n")

            for self.fileext in filename:
                ext1 = pathlib.Path(self.fileext).suffix

                if self.ext == ext1:
                    findext.count += 1
                    findext.fd.write("filename is: %s \n"%self.fileext)

            findext.fd.write("\n")

        findext.fd.write("Total %s file count is: {} \n".format(findext.count)%self.ext)


