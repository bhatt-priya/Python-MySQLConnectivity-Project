import os
import mysql.connector
from tabulate import tabulate
def ViewPurchase():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    item=input("Enter Product Name : ")
    sql="select watch.w_id,watch.brand,purchase.no_of_items,purchase.purchase_date,purchase.amount from watch INNER JOIN purchase ON watch.w_id=purchase.item_id and watch.brand=%s"
    itm=(item,)
    mycursor.execute(sql,itm)
    res=mycursor.fetchall()
    print(tabulate(res,headers=["w_id","brand","date_of_sale","amount"],tablefmt="psql"))
