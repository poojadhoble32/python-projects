'''class Student:
    #non parameterized constructor
    def __init__(self):
        print("this is non prameterized constructor")

    def show(self,name):
        print("hello",name)

sd=Student()
sd.show("pihu")
'''

class Student:
    #non parameterized constructor
    def __init__(self,name):
        print("this is  prameterized constructor")
        self.Cname=name

    def show(self):
        print("hello",self.Cname)

sd=Student("pooja")
sd.show()
