import os
import mysql.connector
from tabulate import tabulate
def Search():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    print("Select the category to display the details")
    print("1. Brand Name")
    print("2. Watch For")
    ch=int(input("Enter your choice to display : "))
    if ch==1:
        val=input("Enter the Brand>?  ")
        st="select * from watch where watch.brand='%s'"%(val)
        mycursor.execute(st)
        data=mycursor.fetchall()
    elif ch==2:
        val=input("You want to display for <Male/ Female>?  ")
        st="select * from watch where w_for='%s'"%(val)
    elif ch==3:
        val=input("Enter colour>?")
        st="select * from watch.colour='%s'"%(val)
        mycursor.execute(st)
        data=mycursor.fetchall()
        print(tabulate(data,headers=["brand","band_type","colour","rate"],tablefmt="psql"))
    else:
        print(error)
    mycursor.execute(st)
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Product_ID","Product_Name","Product_For","Type","Color","Rate"],tablefmt="psql"))

