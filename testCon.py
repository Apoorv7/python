
import mysql.connector#load /import library /module

#establish the connection between python to mysql server
c = mysql.connector.connect(host="localhost",user="root",password="root",database="learning")

#create object of cursor , which can execute/run/fire sql statement
cur = c.cursor()

#execute sql command/statement 
cur.execute("select * from emp")

#read data from cur object 
out  = cur.fetchall()


#iterate the list 
for r in out:
     print(r)
     




