import os
import mysql.connector
def AddProduct():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    
    wid=input("Enter the ID : ")
    wbrand=input("Enter the brand : ")
    wfor=input("Enter Male/Female:")
    bandtype=input("Enter band material:")
    color=input("Enter color:")
    rate=int(input("Enter the Rates for Product :"))
    
    sql= "INSERT INTO watch(w_id,brand,w_for,band_type,colour,rate) VALUES (%s,%s,%s,%s,%s,%s)"
    
    val=(wid,wbrand,wfor,bandtype,color,rate)
    
    mycursor.execute(sql,val)
    
    mycursor.close()
    mydb.commit()
    print("Product inserted ")
