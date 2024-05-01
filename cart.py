import sqlite3
import sys
from user import *
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
    def removeFromCart(self, UserID, ISBN): 
        UserID = input("What is your userID ")
        book = input("what book would you like to remove: ")
        try:
            connection = sqlite3.connect('methods.db')
            cursor = connection.cursor()
            cursor.execute("SELECT ISBN FROM Inventory WHERE Title = ?", (book,))
            ISBN = cursor.fetchone()[0]
            connection = sqlite3.connect('methods.db')
            cursor = connection.cursor()
            cursor.execute("DELETE ISBN FROM Cart WHERE UserID = (?) AND ISBN = ?", (UserID, ISBN))
            connection.commit()
        except Exception as e:
            print("Error removinging items to your order:", e)
        return print("You removed " + book + " to your cart")
    
    def checkOut(self, userID):
        inventory = Inventory()
        order = OrderHistory()
        user = User()
        orderID = order.createOrder(orderID)
        try:
            connection = sqlite3.connect('methods.db')
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Cart WHERE UserID = (?)", (userID,))
            myresult = cursor.fetchall()
            if myresult: 
                #decrease the stock of the orders
                inventory.dereaseStock(x[1],x[2]) 
                #add items to a order
                order.addOderItems(orderID)
                print("Here are your items :) ")
                for x in myresult:
                    print("ISBN:", x[1])
                    print("Quantity:", x[2])
            else:
                print("No items found for this order.")
            #here we are going to check out everything
            cursor.execute("DELETE FROM customers WHERE UserID = ?", (userID,))
            connection.commit()

            cursor.close()
            connection.close()

            print("Checkout successful!")
        except Exception as e:
            print("Error Checking Out", e)
            
