def MobNum():
    
    print("accept 10 digit mobile number")
    a=input()

    if a.isdigit()!=1:
        a=""
        print("please enter only digit values")

    if len(a)!=10:
        a=""
        print("please enter number of length 10:")

    if len(a)==0:    
       return MobNum()

    return a


L=MobNum()

print("your 10 digit mobile number is:",L)


        
