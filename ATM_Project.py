database={'pooja12':{
        'name':'pooja',
        'age':23,
        'email':'pooja34@gmail.com',
        'password':'redhat12',
        'amount':2000,
    },
    'shubs12':{
        'name':'shub',
        'age':22,
        'email':'shub34@gmail.com',
        'password':'redhat13',
        'amount':3000,
    }
          }
print("WELCOME INTO ATM SYSTEM")
print("Enter your choice:")
choice=int(input(" 1.Login \n 2.SignUp \n 3.Exit\nchoice="))
def ATM(choice):
    count=0
    if choice==1:
        print("Enter your name and password:")
        Name=input("Enter name:")
        Password=input("Enter password:")

        for i in database:
            for j,k in i:
                if(i[k]==Name.values() or i[k]==Password.values()):
                    count+=1
                if count==2:
                    print(f"Welcome {name}")
        
ATM(choice)       
