import os
import pathlib


class Find:

    def __init__(self, path, ext1, ext2):
        self.path = path
        self.ext1 = ext1
        self.ext2 = ext2

    def run(self):
        for folder, subfolder, filename in os.walk(self.path):

            for self.fileext in filename:
                self.ext = pathlib.Path(self.fileext).suffix

                if self.ext == self.ext1:
                    i = pathlib.Path(self.fileext).stem + self.ext2

                    fd2 = open(i, 'w')

 
