from urllib import request
import smtplib



class accept:

    body = " Hello Pooja"
    subject = "Test"
    From = "poojadhoble32@gmail.com"
    To = "poojadhoble32@gmail.com"
    print("outside")

    def checkinternetconnection(self):
        print("1")
        try:
            print("2")
            request.urlopen('http://216.58.192.142', timeout=1)
            print("yes")
            return True
        except request.URLError as err:
            print("3")
            print(err)
            return False

