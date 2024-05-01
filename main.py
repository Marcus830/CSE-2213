import sqlite3 as sql
from user import *
from cart import *
from inventory import *
from history import *


## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart()
    inventory = Inventory(user)
    history = OrderHistory()

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory, history)


## incomplete main menu...
def mainMenu(user, cart, inventory, history):
    while(user.getLoggedIn()):
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        print("4. Order Information")
        option = input("Enter your menu choice: ")
        print()

        ## logging out
        if(option == "0"):
            user.logout()

            print("Successful logout.")
        elif(option == "1"):
            user.viewAccountInformation()
        elif(option == "2"):
            print("1. View Inventory")
            print("2. Search Inventory ")
            #print("3. decrese stock")
            print("4. Go Back")
            opt = int(input("pick one: "))
            if(opt == 1):
                inventory.viewInventory(user)
            elif(opt == 2):
                inventory.searchInventory(user)
            #elif(opt == 3):
                #Inventory.dereaseStock(inventory)
            elif(opt == 4):
                mainMenu(user, cart, inventory, history)
            else:
                print("This isn't a vaild option")
        elif(option == "3"):
            print("1. View your Cart")
            print("2. Add to your cart")
            print("3. Remove an item from your cart")   
            print("4. Checkout!!")  
            print("5. Go back")
            opt = int(input("Select a number from (1-3): "))
            if(opt == 1):
                Cart.viewCart(user)
            elif(opt == 2):
                Cart.addToCart(user)
            elif(opt == 3):
                Cart.removeFromCart(user)
            elif(opt == 4):
                confirm = input("Would you like to checkout? (yes/no): ")
                if confirm == "yes":
                    Cart.checkOut(user)
                elif confirm == "No":
                    break
                else:
                    print("this isn't a vaild option")
            elif(opt == 5):
                mainMenu(user, cart, inventory, history)
            else:
                print("this isn't a valid option")
        elif(option == "4"):
            print("1. View Order History")  
            print("2. view Order")
            #print("3. Create an order")
            #print("4. Add items to order")
            opt = int(input("Select a number from (1-3): "))
            userID = user.getUserID()
            if(opt == 1):
                history.viewHistory(userID)
            elif(opt == 2):
                history.viewOrder(user)
            elif(opt == 3):
                history.createOrder(user)
            elif(opt == 4):
                mainMenu(user, cart, inventory, history)
            else:
                print("this isn't a valid option")
        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")
            print()

def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()

           
