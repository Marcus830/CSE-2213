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
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT UserID FROM Cart WHERE userID = ?",)
        result = cursor.fetchall()
        for row in result:
            print(row)
        
    def addToCart(self): 
        UserID = input("What is your userID ")
        ISBN = input("what is the ISBN ")
        quantity = input("what is the quantity ")
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        query = "INSERT INTO Cart (UserID, ISBN, quantity) Values (?,?,?)"
        data = (UserID, ISBN, quantity )
        cursor.execute(query, data)
        connection.commit()
    def removeFromCart(self): 
        UserID = input("What is your userID ")
        ISBN = input("what is the ISBN ")
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        query = "DELETE * FROM Cart WHERE UserID = (?) AND ISBN = ?"
        data = (UserID, ISBN)
        cursor.execute(query,data)
        connection.commit()
    def checkOut(self):
        UserID = input("What is your userID ")
        connection = sqlite3.connect('methods.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cart WHERE UserID = (?)", (UserID,))
        myresult = cursor.fetchall()
        print("Here are your items :) ")
        for x in myresult:
            print(x)
