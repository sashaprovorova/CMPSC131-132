'''
In this program you will create a sales program for a small store. It will track the date and the amount of sales.
It will be capable of inserting, deleting, displaying, and plotting the data which is entered.

Begin by creating a sales class which allows you to store the sales amount in dollars and the date of the sale.
Create the required accessors, mutators, and methods to store and retrieve these values. Next, create an interface
 with a text based menu that allows the use to add, view, delete, and plot the sales figures. You can store the sales
  figures in any of the abstract data types we have studied in this course. Do not use a Python list. You menu might
  look like the following:

-------------------------------------------------------
Menu
-------------------------------------------------------
1) Enter sales data
2) View sales data
3) Delete sales data
4) Plot sales data
5) Exit
-------------------------------------------------------

Enter your choice:

This menu represents the minimum your program should do. Feel free to make your menu more sophisticated, add more
classes,  or word things differently. Do not use a GUI for this assignment.
'''

import matplotlib.pyplot as plt

# creates the sales class
class Sales:
    # method that accepts the sales amount in dollars and the date of the sale as arguments
    def __init__(self, date, amount):
        # definition of data attributes
        self.date = date
        self.amount = amount

    # mutator methods
    def set_amount(self, amount):
        self.amount = amount
    def set_date(self, date):
        self.date = date

    # accesssor methods
    def get_amount(self):
        return self.amount
    def get_date(self):
        return self.date

# initiates the dictionary
mySales = {}

# creates add items method
def addItem(date, amount):
    mySales[date] = Sales(date, amount)

# creates delete items method
def deleteItem(date):
    del mySales[date]

# creates display items method
def display():
    for key in mySales:
        sales = mySales[key]
        print("Date: ", sales.date, end="    ")
        print("Sales amount: ", str(sales.amount), end="    ")
        print(" ")

# method that plots the sales figures
def plotItem():
    arrayForX = []
    arrayForY = []
    for key in mySales:
        sales = mySales[key]
        arrayForX.append(sales.date)
        arrayForY.append(sales.amount)
    plt.plot(arrayForX, arrayForY, c='r', label='Sales')

    plt.title('Sales for the Store', fontsize=20)
    plt.xlabel('Dates', fontsize=18)
    plt.ylabel('Amount in $', fontsize=18)
    plt.legend(loc="center right")
    plt.grid()
    plt.show()

def main():
    # asks the user for data
    continueToAsk = True
    while continueToAsk:
        print(" ")
        print("---------------------\nMenu\n---------------------")
        print("1) Enter sales data\n2) View sales data")
        print("3) Delete sales data\n4) Plot sales data\n5) Exit")
        print("---------------------")

        # calls methods using the attributes entered
        entered = int(input())
        if (entered == 1):
            d = input("Enter the sales date(mm/dd/yyyy):")
            a = float(input("Enter the sales amount in dollars:"))
            addItem(d, a)
        elif (entered == 2):
            display()
        elif (entered == 3):
            s = input("Date:")
            deleteItem(s)
        elif (entered == 4):
            plotItem()
        else:
            continueToAsk = False
main()

