import sqlite3
class Inventory:

    def __init__(self, ISBN, databaseName="methods.db"):
        self.databaseName = databaseName
        self.ISBN = ""
        
    def Inventory(self, databaseName="methods.db"):
        self.ISBN = Inventory.ISBN
        self.Title = Inventory.Title
        self.Author = Inventory.Author
        self.Genre = Inventory.Genre
        self.Pages = Inventory.Pages
        self.ReleaseDate = Inventory.ReleaseDate
        self.Price = Inventory.Price
        self.Stock = Inventory.Stock
     #Done!   
    def viewInventory(self):
        connection = sqlite3.connect("methods.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Inventory ")
        result = cursor.fetchall()
        for row in result:
            print(row)
    #Done!  
    def searchInventory(self):
        userinput = input("What is the title of the book you will like to search for: ")
        conn = sqlite3.connect("methods.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Inventory WHERE Title = ? ", (userinput,))
        myresult = cursor.fetchall()
        print(myresult)
    #Done!
    def dereaseStock(self, quantity=1): 
        #enter the isbn of the stock 
        # fetch the stock number by decrease by 1 
        conn = sqlite3.connect("methods.db")
        cursor = conn.cursor()
        User_ISBN = input("what is the isbn of the book you want to decease? ")
        cursor.execute("Update Inventory SET Stock = Stock - ? WHERE ISBN = ?", (quantity, User_ISBN))
        print("Stock for " + User_ISBN + "has been decreased by "+ quantity)
        conn.commit()
        '''
        try:
            # Connect to the database
            conn = sqlite3.connect("methods.db")
            cursor = conn.cursor()
            # Check with the database if ISBN exists
            User_ISBN = input("what is the isbn of the book you want to decease? ")
            cursor.execute("SELECT * FROM Inventory WHERE ISBN = ? ", (User_ISBN,))
            
            if (User_ISBN == self.ISBN):
                old_stock = cursor.fetchone(Inventory[7])
                New_stock = old_stock - 1
                cursor.execute("Update Inventory SET Stock = ? WHERE ISBN = ?", (New_stock, User_ISBN))
                conn.commit()
            #Userinput = ISBN
            #print(Userinput)

            if(Userinput == Inventory.ISBN):
                Inventory.Stock = Inventory.Stock - 1
            cursor.execute("Update Inventory SET Stock = Stock - ? WHERE ISBN = ?", (quantity, ISBN))
            conn.commit()
                #print(Inventory.Stock)
            # Decrease the stock for the given ISBN by the specified quantity
            #print(f"Stock for ISBN {ISBN} decreased by {quantity}.")

        except sqlite3.Error as e:
            print("Error accessing database:", e)
                # Close the connection
            if conn:
                conn.close()
        '''
