import os                                                                 
import mysql.connector
def editproduct():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    wid=input("Enter product ID to be edited : ")
    sql="select * from watch where w_id=%s"
    a=(wid,)
    mycursor.execute(sql,a)
    b=mycursor.fetchall()
    for i in b:
        print(i)
    fld=input("Enter the field which you want to edit : ")
    val=input("Enter the value you want to set : ")
    sql="Update watch set  " + fld +"='" + val + "' where w_id='" +wid+"'"
    sq=sql
    mycursor.execute(sql)
    print("Okay! Your Editing is done:) ")
    print("After correction the record is : ")
    sql="select * from watch where w_id=%s"
    a=(wid,)
    mycursor.execute(sql,a)
    b=mycursor.fetchall()
    for i in b:
        print(i)
    mycursor.close()
    mydb.commit()


