import sqlite3
class Inventory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        
        #def Inventory("methods.db"):
            #return Inventory
        
    def viewInventory(self):
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Inventory ")
        result = cursor.fetchall()
        for row in result:
            print(row)
        
    def searchInventory(self):
        userinput = input("What is the title of the book you will like to search for: ")
        conn = sqlite3.connect("methods.db")
        mycursor = conn.cursor()
        sql = "SELECT * FROM Inventory WHERE Title LIKE '%{userinput}%'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        
    def dereaseStock(self, ISBN, quantity=1):
        try:
            # Connect to the database
            conn = sqlite3.connect("methods.db")
            cursor = conn.cursor()

            # Decrease the stock for the given ISBN by the specified quantity
            cursor.execute("DELETE items SET stock = stock - ? WHERE ISBN = ?", (quantity, ISBN))
            conn.commit()

            print(f"Stock for ISBN {ISBN} decreased by {quantity}.")

        except sqlite3.Error as e:
            print("Error accessing database:", e)
                # Close the connection
            if conn:
                conn.close()
