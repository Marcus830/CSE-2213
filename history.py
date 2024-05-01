import sqlite3
import random
import datetime
class OrderHistory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        self.OrderNumber = ""

    def getOrderNumber(self):
        return self.OrderNumber
    
    #Done!
    def viewHistory(self, userID):
        try:
            connection = sqlite3.connect("methods.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Orders WHERE userID = ?", (userID))
            result = cursor.fetchone()
            if result:
                print(result)
            else:
                print("Order not found")
            cursor.close()
            connection.close()
        except Exception as e:
            print("ERROR viewing your order details:",e)

    #Done!
    def viewOrder(self, userID, OrderNumber):
        try:
            connection = sqlite3.connect("methods.db")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM orders WHERE userID = ? AND orderNumber = ?",(userID, OrderNumber, ) )
            result = cursor.fetchone()
            if result:
                print(f"Details for Order ID {userID}:")
                print("Your Order:", result[1] + result[2] + result[3] + result[4])
            else:
                print("Order not found.")

            cursor.close()
            connection.close()
        except Exception as e:
            print("Error viewing order details:", e)

    
    def createOrder(self, userID, quantity, cost, date):
        try:
            connection = sqlite3.connect("methods.db")
            cursor = connection.cursor()

        # This is going to give a new and unique orderID
            orderID = str(random.randint(100000, 999999))  # Example random orderID
            while True:
                cursor.execute("SELECT * FROM Orders WHERE orderNumber = ?", (orderID,))
                Used_order = cursor.fetchone()
                if Used_order:
                    orderID = str(random.randint(100000, 999999))
                else:
                    break

            cursor.execute("INSERT INTO Orders (OrderNumber, UserId, ItemNumber, Cost, Date) VALUES (?, ?, ?, ?, ?)", (orderID, userID, quantity, cost, date),)
            connection.commit()

            print("Order created with ID:", orderID)

            cursor.close()
            connection.close()

            return orderID
        except Exception as e:
            print("Error creating order:", e)
        return None

    
    def addOrderItems(self, orderID, userID):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO OrderItems (orderID, userID) SELECT ?, item_id, item_name, quantity, price FROM cart WHERE user_id = ?",
                (orderID, userID),
            )
            connection.commit()

            print(f"Items added to Order ID {orderID}.")

            cursor.close()
            connection.close()
        except Exception as e:
            print("Error adding order item:", e)