import os
import sys
from easygui import passwordbox
import addproduct
import editproduct
import delproduct
import viewpurchase
import viewproduct
import viewcustomer
import custdet
import purchaseproduct
import searchproduct
import graph

name=input("ENTER YOUR NAME :")
print("")
print("HELLO,",name)
print("")
print("")
f=open("head.txt","r")
file=f.read()
print(file)
f.close()
ans="y"
while True:
    f=open("first.txt","r")
    file=f.read()
    print(file)
    f.close()
    choice=int(input("Enter your choice:"))
    print("")

    if (choice==1):
        password=passwordbox("Enter password:")
        print(" PASSWORD SUCCESSFULLY ENTERED")
        if password=="a":
            print("")
            print(":)-------------YOU WANT-------------:)")
            f=open("second.txt","r")
            file=f.read()
            print(file)
            f.close()
        else:
            print("Invalid password",name)
            sys.exit()
        while True:
            print("")
            c=int(input("Enter your choice:"))
            if(c==1):
                addproduct.AddProduct()
                break
            elif(c==2):
                editproduct.editproduct()
                break
            elif(c==3):
                delproduct.DelProduct()
                break
            elif(c==4):
                viewproduct.ViewProduct()
                break
            elif(c==5):
                viewpurchase.ViewPurchase()
                break
            elif(c==6):
                custdet.customer_det()
                break
            elif(c==7):
                graph.Graph()
            else:
                print("Invalid choice")
        ans=input("Do you want to run again?<y/n>:")
        if ans=="n":
            print("")
            print("Its a good day to have a good day! :)")
            sys.exit()

    elif (choice==2):
        print("")
        print("-------------YOU WANT-------------")
        f=open("third.txt","r")
        file=f.read()
        print(file)
        f.close()
        while True:
            ch=int(input("Enter your choice:"))
            if(ch==1):
                viewproduct.ViewProduct()
                break
            elif(ch==2):
                searchproduct.Search()
                break
            
            elif(ch==3):
                purchaseproduct.PurchaseProduct()
                break
            else:
                print("Invalid choice")
        ans=input("Do you want to run again?<y/n>:")
        if ans=="n":
            print("")
            print("Its a good day to have a good day! :)")
            sys.exit()
    else:
        print("* * * * * * * * * *INVALID CHOICE* * * * * * * * * *")
        print("")
        ans=input("Do you want to run again?<y/n>:")
