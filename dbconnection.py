import mysql.connector

myconn=mysql.connector.connect(host = "localhost",user = "root",passwd = "root")

print(myconn)

cur = myconn.cursor()

print(cur)
