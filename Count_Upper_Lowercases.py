string1=input("accept string:")

def Count_Upper_Lower(string2):
    Lower=0
    Upper=0
    Spl=0

    for i in string2:
        if i>='a' and i<='z':
            Lower+=1
        elif i>='A' and i<='Z':
            Upper+=1
        else:
            Spl+=1

    print(f"In this string lower letters are {Lower},upper letters are {Upper},and Special char are {Spl}")
    

Count_Upper_Lower(string1)

