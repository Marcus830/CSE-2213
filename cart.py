import sqlite3
import sys
class Cart:

    def __init__(self, databaseName = "methods.db"):
        self.databaseName = "methods.db"

    def Cart():
        pass
    def Cart(self):
        try:
            connection = sqlite3.connect("methods.db")
            print("Successful connection.")
        except:
            print("Failed connection.")
            sys.exit()
    def viewCart(self, userID): 
        userID = input("what is your userID? ")
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cart WHERE userID = ?", userID)
        result = cursor.fetchall()
        for row in result:
            print(row)
        
    def addToCart(self, UserID, ISBN, quantity): 
        UserID = input("What is your userID")
        ISBN = input("what is the ISBN")
        quantity = input("what is the quantity")
    def removeFromCart(self, userID, ISBN): 
        pass
    def checkOut(self, userID):
        pass
