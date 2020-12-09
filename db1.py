import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database = "Pythondb")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
    dbs = cur.execute("create table Employee3(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")  
except:  
    myconn.rollback()

sql = "insert into Employee3(name, id, salary, dept_id, branch_name) values (%s, %d, %d, %s, %s)"  
  
#The row values are provided in the form of tuple   
  
val = ("John", 102, 25000,234,"debt")  
try:  
    #inserting the values into the table  
    cur.executemany(sql,val)  
  
    #commit the transaction   
    myconn.commit()  
      
except:  
    myconn.rollback()  
  
print(cur.rowcount,"record inserted!")
 
try:  
    #Reading the Employee data      
    cur.execute("select * from Employee")  
  
    #fetching the rows from the cursor object  
    result = cur.fetchone()  
    #printing the result  
      
    for x in result:  
        print(x);  
except:  
    myconn.rollback()  


  
myconn.close()  
 
