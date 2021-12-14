import os
import mysql.connector
from tabulate import tabulate
def ViewProduct():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    mycursor.execute("select * from watch")
    data=mycursor.fetchall()
    print(tabulate(data,headers=["w_id","brand","w_for","band_type","colour","rate"],tablefmt="psql"))
    
