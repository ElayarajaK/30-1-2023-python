import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "raja_db")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
  
    #Reading the Employee data      
    cur.execute("select name, id, salary from Employee")  
  
    #fetching the rows from the cursor object  
    result = cur.fetchall()  
  
    print("Name    id    Salary");  
    for row in result:  
        print("%s    %d    %d"%(row[0],row[1],row[2]))  
except:  
    myconn.rollback()  
  
myconn.close()  
