import sqlite3
import random
import datetime
class OrderHistory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName

    #def getUserID(self):
        #return self.userID
    
    def Orders(self, databaseName="methods.db"):
        '''
        self.ISBN = Orders.ISBN
        self.Title = Orders.Title
        self.Author = Orders.Author
        self.Genre = Orders.Genre
        self.Pages = Orders.Pages
        self.ReleaseDate = Orders.ReleaseDate
        self.Price = Orders.Price
        self.Stock = Orders.Stock
        '''

    #Done!
    def viewHistory(self, userID):
        try: 
            connection = sqlite3.connect("methods.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Orders")
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(row)
            else: 
                print("There was a order for this user")
        except Exception as e:
            print("Error Checking Out", e) 

    #Done!
    def viewOrder(self, userID):
        try:
            connection = sqlite3.connect("methods.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Orders WHERE userID = ?", (userID,))
            result = cursor.fetchone()
            if result:
                print(result)
            else:
                print("Order not found")
            cursor.close()
            connection.close()
        except Exception as e:
            print("ERROR viewing your order details:",e)
    
    def createOrder(self, userID, quantity, cost, date):
        try:
            connection = sqlite3.connect(self.databaseName)
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