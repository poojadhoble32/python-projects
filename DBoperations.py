import mysql.connector

mycon=mysql.connector.connect(host="localhost",user="root",passwd="root",database="pythondb")

print(mycon)

cur=mycon.cursor()

print(cur)

try:
    cur.execute("create database pythondb")
    cur.execute("show databases")

except:
    mycon.rollback()

for x in cur:
    print(x)
try:
    cur.execute("create table student(rollno int primary key,name varchar(20) not null,lastname varchar(20) not null,birthdate date not null")
except:
    mycon.rollback()

sql="insert into student(rollno,name,lastname,birthdate)values(%d,%s,%s,%s)"

val=(1,'pooja','dhoble','21/09/1997')

try:
    cur.execute(sql,val)
    #mycon.commit()
except:
    mycon.rollback()

print(cur.rowcount,"record inserted!")

val=[(2,'ravi','shinde','21/08/1997'),(3,'nisha','mali','21/07/1997'),(4,'gita','sane','21/11/1997'),(5,'piyush','dere','21/04/1997')]

try:
    cur.executemany(sql,val)
    mycon.commit()
except:
    mycon.rollback()

print(cur.rowcount,"record inserted!")
print(cur.rowcount,"record inserted!",cur.lastrowid)

try:
    cur.execute("select * from student")
    result=cur.fetchall()

    for x in cur:
        print(x)
except:
    mycon.rollback()





                      
mycon.close()
