"""
Design an inventory class that stores the following members:

serialNum: An integer that holds a part's serial number.
manufactDate: A member that holds the date the part was manufactured.
lotNum: An integer that holds the part's lot number.
The class should have appropriate setter and getter functions.

Next, design a stack class that can hold objects of the class described above. If
you wish, you may use the linked list from program 5 as a basis for designing your
stack.

Finally, design a program that uses the stack class described above. The program
should have a loop that asks the user if he or she wishes to add a part to
inventory, or take a part from inventory. The loop should repeat until the user
is finished. If the user wishes to add a part to inventory, the program should
ask for the serial number, date of manufacture, and lot number. The data should
be stored in an inventory object, and the object should be pushed onto the stack.
If the user wishes to take a part from inventory, the program should pop the
top-most part from the stack. When the user finishes the program, it should
display the contents of the member values of all the objects that remain on the stack.
"""
#base class
class inventory():
    #creates a method that accepts three arguments
    def __init__(self, serialNum, manufactDate, lotNum):
        self.__serialnum=serialNum
        self.__manufactDate=manufactDate
        self.__lotNum=lotNum
        
    #creates mutator methods
    def set_sNumber(self, serialnum):
        self.__serialnum=serialNum
    def set_mDate(sellf, manufactDate):
        self.__manufactDate=manufactDate
    def set_lNum(self, lotNum):
        self.__lotNum=lotNum
        
    #creates accesssor methods
    def get_sNumber(self):
        return self.__serialnum
    def get_mDate(self):
        return self.__manufactDate
    def get_lNum(self):
        return self.__lotNum

#Node from program 5
class Node:
    
    #creates a method that accepts the data as an argument
    def __init__(self,data):
        #defines data attributes
        self.data=data
        self.next=None

    #creates mutator methods
    def set_data(self, new_data):
        self.data=new_data
    def set_next(self, new_next):
        self.next=new_next

    #creates accesssor methods
    def get_data(self):
        return self.data
    def get_next(self, new_next):
        return self.next
 
#stack class
class Stack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items==[]

#main function
def main():
    
    #calls the stack method
    stack=Stack()
    
    check=True
    
    while check:
        #requests the information from the user
        entered=input("Wish to add a part to inventory, or take a part from inventory?\nType \"take\" or \"add\". ")
        #pushes the objects onto the stack
        if entered == "add" or entered=="Add":
            ent=int(input("Enter a serial number: "))
            ent2=input("Enter manufacturing date: ")
            ent3=int(input("Enter lot number: " ))
            stack.push(ent)
            stack.push(ent2)
            stack.push(ent3)
            print("")
        #pops the object from the stack    
        elif entered =="take" or entered=="Take":
            stack.pop()
            print("")
            
        #displays the remaining objects and ends the program   
        else:
            print(" ")
            print("Objects that remain on the stack: ")
            print(stack.items)
            check=False

main()
    

  
    
