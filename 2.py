class bankaccount:
    
    ROI = 10.5
    
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        
    def display(self):
        print("amount in {} account is {}".format(self.name,self.amount))
        
    def withdraw(self):
        print("enter amount to withdraw from user account:")
        self.withdraw1 = int(input())
        self.amount = self.amount - self.withdraw1
        print("amount after withdraw:",self.amount)
    
    def diposit(self):
        print("enter amount to deposit in user account:")
        self.amount1 = int(input())
        self.amount = self.amount + self.amount1
        print("amount after diposit:",self.amount)
    
    def calculateinterest(self):
        print("enter amount to find interest:")
        self.value = int(input())
        self.interestamount = self.value * (bankaccount.ROI/100)
        print("calculated interest amount is:",self.interestamount)
    
    
def accept():

    print("enter name of account holder:")
    name = input()
    
    print("enter amount to store in account:")
    amount = int(input())
    
    obj1 = bankaccount(name,amount)
    
    obj1.diposit()
    obj1.withdraw()
    obj1.calculateinterest()
    obj1.display()
    
if __name__ == "__main__":
    accept()
    
