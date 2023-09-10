import FindFilesExtension
import LogFile

def Template():
    #print("Enter Dir/path :")
    path = "DemoFolder"            #pathname

    #print("Enter file extension to search files :")
    ext = ".txt"                     #file extension to search

    lf = LogFile.LogFile()
    seperation = "-" * 100
    lf.WriteLog(seperation)
    lf.WriteLog("Log files which containing %s extension"%ext)
    lf.WriteLog(seperation)

    ffe = FindFilesExtension.DirectoryWatcher(path,ext)  # class obj creation

    ffe.Watcher()   # funccall
