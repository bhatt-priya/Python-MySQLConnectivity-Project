import os
import mysql.connector
from tabulate import tabulate

def customer_det():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="suchika",database="cs")
    mycursor=mydb.cursor()
    mycursor.execute("select * from customer")
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Name","Phone Number","Age","Address"],tablefmt="psql"))

