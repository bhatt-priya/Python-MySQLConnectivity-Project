import mysql.connector
import datetime
import matplotlib.pyplot as plt
def Graph():
    mydb= mysql.connector.connect(host="localhost",user="root",passwd="priya",database="cs")
    mycursor=mydb.cursor()
    mycursor.execute("Select sum(amount),Purchase_date from purchase group by Purchase_date")
    myrecords=mycursor.fetchall()
    Purchase_date=[]
    amount=[]
    for i in range (len(myrecords)):
        Purchase_date.append(myrecords[i][0])
        amount.append(myrecords[i][1])
    plt.plot(amount,Purchase_date,marker='o')
    plt.title("DAILY SALES")
    plt.xlabel("Date of sale")
    plt.ylabel("Sales")
    plt.show()
