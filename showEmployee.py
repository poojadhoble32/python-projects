class A:
    Name="\0"
    Salary=0
    
    def showEmployee(self,Name,Salary=50000):
        print(f"{Name}:{Salary}")

obj=A()

obj.showEmployee("Pooja")
