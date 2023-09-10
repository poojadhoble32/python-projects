def Area(radius=22,pi=3.14):                 #default arg
    area=radius*radius*pi
    return area

def main():
    rvalue= 30
    pivalue=3.14

    ans= Area(radius=rvalue,pi=pivalue)     #keyword arg
    print("area is:",ans)
    
    ans= Area(30)     #default call radius = 30.33 pi=3.14
    print("area is:",ans)
    
    ans= Area(pi=3.14)     #keyword arg
    print("area is:",ans)

if __name__=="__main__":
    main()