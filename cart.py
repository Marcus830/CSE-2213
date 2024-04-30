import sqlite3
import sys
from inventory import *
from history import *
class Cart:

    def __init__(self, databaseName = "methods.db"):
        self.databaseName = "methods.db"

    #def getUserID(self):
        #return self.userID
    def Cart():
        pass
    def Cart(self):
        try:
            connection = sqlite3.connect("methods.db")
            print("Successful connection.")
        except:
            print("Failed connection.")
            sys.exit()

    #Done!
    def viewCart(self): 
        userID = input("What is your userID ")
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cart WHERE userID = ?",(userID,))
        result = cursor.fetchall()
        for row in result:
            print(row) 
     # DONE!   
    def addToCart(self): 
        UserID = input("What is your userID ")
        book = input("what is the book ")
        quantity = 1
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        cursor.execute("SELECT ISBN FROM Inventory WHERE Title = ?", (book,))
        ISBN = cursor.fetchone()[0]
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Cart (UserID, ISBN, quantity) Values (?,?,?)", (UserID, ISBN, quantity))
        connection.commit()
        return print("You added " + book + " to your cart")
    def removeFromCart(self): 
        UserID = input("What is your userID ")
        book = input("what book would you like to remove: ")
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        cursor.execute("SELECT ISBN FROM Inventory WHERE Title = ?", (book,))
        ISBN = cursor.fetchone()[0]
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        cursor.execute("DELETE ISBN FROM Cart WHERE UserID = (?) AND ISBN = ?", (UserID, ISBN))
        connection.commit()
        return print("You removed " + book + " to your cart")
    
    def checkOut(self):
        UserID = input("What is your userID ")
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        #create a new order 
        OrderHistory.createOrder()
        #add items to a order
        OrderHistory.addOderItems()
        #decrease the stock of the orders
        Inventory.dereaseStock()
        cursor.execute("SELECT * FROM Cart WHERE UserID = (?)", (UserID,))
        myresult = cursor.fetchall()
        print("Here are your items :) ")
        for x in myresult:
            print(x)
        #here we are going to check out everything
        cursor.execute("DELETE FROM customers WHERE UserID = ?", (UserID,))
