import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "raja_db")  
#creating the cursor object  
cur = myconn.cursor()  
sql = "insert into Employee(name, id, salary, dept_id) values (%s, %s, %s, %s)"  
  
#The row values are provided in the form of tuple   
val = ("John", 110, 25000.00, 201)  
  
try:  
    #inserting the values into the table  
    cur.execute(sql,val)  
  
    #commit the transaction   
    myconn.commit()  
      
except Exception as e:
    print(e);  
    myconn.rollback()  
  
print(cur.rowcount,"record inserted!")  
myconn.close()  
