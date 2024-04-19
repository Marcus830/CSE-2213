import sqlite3
import random
class OrderHistory:

    def __init__(self, OrderHistory, viewHistory, viewOrder, createOrder, addOrderItems):
        self.OrderHistory = OrderHistory
        self.viewHistory = viewHistory
        self.viewOrder = viewOrder
        self.createOrder = createOrder
        self.addOderItems = addOrderItems

    def OrderHistory():
        return OrderHistory
    
    def viewHistory(userID):
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Orders ")
        result = cursor.fetchall()
        for row in result:
            print(row)

    def viewOrder():
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT {userID} FROM Orders ")
        result = cursor.fetchone()
        for row in result:
            print(row)
    
    def createOrder(string userID, int quantity, float cost, string date):
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

        while(1):
            selection = input("What books would like to add:")
            quantity = input("How many would you like? ")
            date = input("what is today's date")
            if (selection == "done"):
                break
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
    
    def addOderItems(string userID, string orderID):
        # question do we have to ask for the userID? 
        
        #here her we would jions the items from the oderitems to the cart
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        orderitems = "SELECT OrderItems.OrderNumber, OrderItems.ISBN, OrderItems.Quantity FROM OrderItems INNER JOIN Cart ON Cart.UserID=OrderItems.OrderNumber;"
        cursor.executemany(orderitems)
        connection.commit() 

