import os
import mysql.connector
from tabulate import tabulate
def DelProduct():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    wid=input("Enter the id to be deleted : ")
    id=(wid,)
    sql="delete from purchase where item_id=%s"
    mycursor.execute(sql,id)
    mydb.commit()
    sql="delete from watch where w_id=%s"
    mycursor.execute(sql,id)
    mydb.commit()
    print("One Item Deleted")
