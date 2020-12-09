import mysql.connector

mycon=mysql.connector.connect(host="localhost",user="root",passwd="root",database="pythondb")

print(mycon)

cur=mycon.cursor()

print(cur)


try:
    dbs=cur.execute("create table student2(rollno int primary key,name varchar(20) not null,lastname varchar(20) not null");
except:
    mycon.rollback()

sql="insert into student2(rollno,name,lastname,birthdate)values(%d,%s,%s)"

val=[(3,'nisha','kale'),(4,'gita','sane'),(5,'piyush','dere')]

try:
    dbs=cur.executemany(sql,val)
    mycon.commit()
except:
    mycon.rollback()

print(cur.rowcount,"record inserted!",cur.lastrowid)
try:
    cur.execute("select * from student2")
    result=cur.fetchall()

    for x in result:
        print(x)
except:
    mycon.rollback()

mycon.close()

