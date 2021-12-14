import os
import mysql.connector
def ViewCustomer():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    name=input("Enter your name:")
    while True:
        phone=input("Enter your phone number(10-digits):")
        num=str(phone)
        if len(num)==10:
            break
        else:
            print("Please enter valid phone number!")
    age=int(input("Enter your age:"))
    add=input("Enter your address:")
    sql= "INSERT INTO customer(Name,Phone_Number,Age,Address) VALUES (%s,%s,%s,%s)"
    val=(name,num,age,add)
    mycursor.execute(sql,val)
    mycursor.close()
    mydb.commit()
    print("THANKYOU!")
