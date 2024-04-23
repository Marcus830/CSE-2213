import sqlite3
import random
class OrderHistory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
    #def OrderHistory():
        #return OrderHistory
    
    def viewHistory(self, userID):
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Orders ")
        result = cursor.fetchall()
        for row in result:
            print(row)

    def viewOrder(self, userID, orderID):
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Orders WHERE userID = ?", userID)
        result = cursor.fetchone()
        print(result)
    
    def createOrder(self, userID, quantity, cost, date):
        # I'm going to ask what is their userid
        userID = input("What is your userID:")
        # generate a new orderID 
        newOrderID = str(random.randint(10,99)) + "-" + str(random.randint(1000,9999))
        # ask what items the user would want and how many, I guess we would use update
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Inventory ")
        result = cursor.fetchone()
        for row in result:
            print(row)
        selection = input("What books would like to add:")
        quantity = input("How many would you like? ")
        date = input("what is today's date")
        if selection == "done":
            print("adding to your order now")
         #insert those items into the database
        items = "INSERT INTO Orders (OrderNumber, UserID, ItemNumber, Cost, Date) VALUES (?, ?, ?, ?, ?)"
        cursor.excuteone(items)
        connection.commit()
        # add up the cost of the items 
        data = "SELECT SUM Cost FROM Order WHERE {newOderID} "
        cursor.executemany(data)
        connection.commit() 
        # we would return date, orderID, cost, and items 
        return "SELECT * FROM ORDERS"
    
    def addOderItems(self, userID, orderID):
        # question do we have to ask for the userID? 

        #here her we would jions the items from the oderitems to the cart
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        orderitems = "SELECT OrderItems.OrderNumber, OrderItems.ISBN, OrderItems.Quantity FROM OrderItems INNER JOIN Cart ON Cart.UserID=OrderItems.OrderNumber;"
        cursor.executemany(orderitems)
        connection.commit() 

