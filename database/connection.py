import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='asish',password='root',database='asish')
mycursor = mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
    print(i)