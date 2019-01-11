import mysql.connector

mydb=mysql.connector.connect(host="localhost",user='root',passwd='root',database='telusko')

mycursor = mydb.cursor()

#mycursor.execute("show databases")

mycursor.execute("select * from student")


result = mycursor.fetchall()

result1 = mycursor.fetchone()

for i in mycursor:
	print(i)