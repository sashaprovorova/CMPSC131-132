'''
Create a class called inventory item that has the following data attributes:

UPC Number
Price
Cost
Quantity on hand
Next, write a program which allows the user to manage the inventory. The program,
at a minimum, should allow the user to:

Add an item to the inventory
Delete an item from the inventory
Modify an item in the inventory

Display the entire inventory in a simple table (print statements which puts the
inventory into columns). Store that inventory item in a dictionary. Use the UPC
Number as a key. You can assume that every inventory item has a unique UPC number.
Your program must use a simple menu structure similar to this:

-------------------------------------------------------
Menu
-------------------------------------------------------
1) Add an item to the inventory
2) Delete an item from the inventory
3) Modify an item from the inventory
4) Display the inventory
5) Exit
-------------------------------------------------------

Enter your choice:

This menu represents the minimum your program should do. Feel free to make your
menu more sophisticated, add more classes,  or word things differently. Do not
use a GUI for this assignment.
'''
#base class
class inventoryItem:
    #creates a method that accepts four arguments
    def __init__(self, upc, price, cost, quantity):
        self.upc=upc
        self.price=price
        self.cost=cost
        self.quantity=quantity

    #creates mutator methods
    def set_upc(self, upc):
        self.upc=upc
    def set_price(sellf, price):
        self.price=price
    def set_cost(self, cost):
        self.cost=cost
    def set_quantity(self, quantity):
        self.quantity=quantity

    #creates accesssor methods
    def get_upc(self):
        return self.upc
    def get_price(self):
        return self.price
    def get_cost(self):
        return self.cost
    def get_quantity(self):
        return self.quantity

#main function
def main():

    #initiates the dictionary
    myInventory={}

    #creates add items method
    def addItem(upc, price, cost, quantity):
        myInventory[upc]=inventoryItem(upc, price, cost, quantity)

    #creates delete items method
    def deleteItem(upc):
        del myInventory[upc]

    #creates modify items method
    def modifyItem(upc, price, cost, quantity):
        myInventory[upc]=inventoryItem(upc, price, cost, quantity)
        
    #creates display items method
    def display():
        
        for key in myInventory:
            inventory = myInventory[key]
            print ("UPC: ", inventory.upc, end = "    ")
            print ("Price: ", str(inventory.price), end = "    ")
            print ("Cost: ", str(inventory.cost), end = "    ")
            print ("Quantity: ", str(inventory.quantity))

    #asks the user for data
    continueAsk=True
    while continueAsk:
        
        print ("---------------------\nMenu\n---------------------")
        print ("1) Add an item to the inventory\n2) Delete an item to the inventory")
        print ("3) Modify an item to the inventory\n4) Display the inventory\n5) Exit")
        print ("---------------------")

        #calls methods using the attributes entered  
        entered = int(input())
        if (entered == 1):
            u = input("UPC:")
            p = float(input("Price:"))
            c = float(input("Cost:"))
            q = int(input("Quantity:"))
            addItem(u, p, c, q)
        elif (entered == 2):
            u = input ("UPC:")
            deleteItem (u)    
        elif (entered == 3):
            u = input("UPC:")
            p = float(input("Price:"))
            c = float(input("Cost:"))
            q = int(input("Quantity:"))
            modifyItem(u, p, c, q)
        elif (entered == 4):
            display()                  
        else:
            continueAsk=False

main()






    

    








        
    
