
class LogFile:
    fd = open("LogFile.log", "w")

    def WriteLog(self,msg):
        self.msg=msg

        LogFile.fd.write(self.msg)
        LogFile.fd.write("\n")




