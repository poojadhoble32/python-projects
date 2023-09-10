import os
import pathlib
import LogFile
import WriteToCsv

class DirectoryWatcher:
    L = []   #class instance

    def __init__(self, dirname, extname):
        self.dirname = dirname
        self.extname = extname

    def Watcher(self):

        flag = os.path.isabs(self.dirname)  # isabs = checks is it whole path or not or just directory
        #print(flag)

        if flag == False:
            self.dirname = os.path.abspath(self.dirname)  # abspath = convert directory into absolute path if path is not abs
        #print(self.dirname)

        exist = os.path.isdir(self.dirname)  # checks whether given directory is exist?
        #print(exist)
        lf = LogFile.LogFile()      #logfile class obj

        if exist:
            self.count = 0
            #print("exist")
            for root, dirs, files in os.walk(self.dirname):  # fetch all dir,subdir,files names
                for f in files:
                    fext = pathlib.Path(f).suffix  #save only extension from file
                    #print(fext)
                    if fext == self.extname:
                        self.count+=1
                        lf.WriteLog(str(self.count)+")\t"+f+"\n")
                        DirectoryWatcher.L.append(f)

        wtc = WriteToCsv.WriteToCsv()
        wtc.CsvFile(DirectoryWatcher.L)
        #print(DirectoryWatcher.L)
