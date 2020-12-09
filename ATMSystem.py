database={1001:{'name':'pooja',
                'age':23,
                'email':'pooja@gmail.com',
                'password':1234,
                'amount':6000
               },
          1002:{'name':'nishan',
                'age':35,
                'email':'nishan@gmail.com',
                'password':5678,
                'amount':15000
               }
         }

i=int(input(" 1.signin\n 2.sign up\n 3.Exit\nEnter your choice: "))

if(i==1):
    
    account=int(input("Enter Account Number:"))
    passkey=int(input("Enter password:"))
    
    if(account in database.keys() and passkey==database[account]['password']):
        
        print("welcome",database[account]['name'])

        j=int(input("1.check balance\n2.Deposit balance\n3.withdrawal\n4.logout\nEnter your choice:"))

        while (j<5 and j>0):

            if(j==1):
                print("Your balance:",database[account]['amount'])
                
            elif(j==2):
                y=int(input("Enter deposit amount:"))
                database[account]['amount']=database[account]['amount']+y
                
            elif(j==3):
                z=int(input("Enter withdraw amount"))
                print("collect your cash:",z)
                database[account]['amount']=database[account]['amount']-z
                
            else:
                print("sucessfully logged out")
                break

            j=int(input("1.check balance\n2.Deposit balance\n3.withdrawal\n4.logout\nEnter your choice:"))

    else:
        print("wrong password")

elif(i==2):

    print("enter your details:")

    account=int(input("enter the account number:"))
    Name=input("enter your name:")
    Age=int(input("enter your age:"))
    Email=input("enter your email id:")
    Password=int(input("enter password:"))
    Amount=int(input("enter your amount:"))

    database.update({account:{'name':Name,'age':Age,'email':Email,'password':Password,'amount':Amount}})
                
    print(database)
    print("account is updated successfully")

else:
    print("exited successfully")
