import sqlite3
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
    def viewHistory(self):
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Orders ")
        result = cursor.fetchall()
        for row in result:
            print(row)
    #Done!
    def viewOrder(self):
        userID = input("What is your userID: ")
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Orders WHERE userID = ?", (userID,))
        result = cursor.fetchone()
        print(result)
    
    def createOrder(self, userID, quantity, cost):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()

            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("INSERT INTO orders (user_id, quantity, cost, date) VALUES (?, ?, ?, ?)", (userID, quantity, cost, order_date),)
            connection.commit()

            orderID = cursor.lastrowid
            print("Order created with ID:", orderID)

            cursor.close()
            connection.close()

            return orderID
        except Exception as e:
            print("Error creating order:", e)
            return None

    
    def addOrderItems(self, orderID, item_id, item_name, quantity, price):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO order_items (order_id, item_id, item_name, quantity, price) VALUES (?, ?, ?, ?, ?)",
                (orderID, item_id, item_name, quantity, price),
            )
            connection.commit()

            print(f"Item '{item_name}' added to Order ID {orderID}.")

            cursor.close()
            connection.close()
        except Exception as e:
            print("Error adding order item:", e) 