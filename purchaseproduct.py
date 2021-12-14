import os
import mysql.connector
from tabulate import tabulate
import viewcustomer
import datetime
import time
import custdet
def PurchaseProduct():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    mn=""
    dy=""
    now=datetime.datetime.now()
    wid="P"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    L=[]
    Lst=[]
    L.append(wid)
    itemId=input("Enter Product ID : ")
    L.append(itemId)
    itemNo=int(input("Enter the number of Items : "))
    L.append(itemNo)
    sql="select rate from watch where w_id=%s"
    wid=(itemId,)
    mycursor.execute(sql,wid)
    b=mycursor.fetchone()
    for x in b:
        print("rate is : ", x)
    amount=x*itemNo
    L.append(amount)
    mnth=now.month
    if mnth<=9:
        mn="0"+str(mnth)
    else:
        mn=str(mnth)
        day=now.day
    if day<=9:
        dy="0"+str(day)
    else:
        dy=str(day)
    dt=str(now.year)+"-"+mn+"-"+dy
    L.append(dt)
    tp=(L)
    sql="insert into purchase(purchase_id,item_id,no_of_items,amount,Purchase_date)values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tp)
    mydb.commit()
    
    
    print("Please fill mandatory details below.")
    viewcustomer.ViewCustomer()
    print("")
    print("SIT BACK AND RELAX TILL WE GENERATE YOUR BILL!")
    time.sleep(2)
    print("Loading....!")
    time.sleep(2)
    print("===========================================================================================")
    print("                                 UNIQUE WATCH STORE                                        ")
    print("                                                                                           ")
    print("===========================================================================================")
    
    print("                                                                                           ")
    print("                         ","YOUR GRAND TOTAL= RS.",amount,"                                ")
    print("                                                                                           ")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-THANKYOU AND PLEASE VISIT AGAIN *-*-*-*-*-*-*-*-*-*-*-*-* ")
    print("===========================================================================================")
    mycursor.close()
    mydb.commit()
