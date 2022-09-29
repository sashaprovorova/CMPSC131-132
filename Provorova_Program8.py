'''
Design an EmployeeInfo class that holds the following employee information:

Employee ID Number
Employee Name

Next implement a binary search tree whose nodes hold an instance of the
EmployeeInfo class. The nodes should be sorted on the Employee ID number.
Test the binary tree by inserting nodes with the following information. You
can manually enter the information in code or you can prompt the user with a
menu system.

Finally, your program should allow the user to enter an ID number, then search
the tree for the number. If the number is found, it should display the employee’s
name. If the node is not found, it should display a message indicating so.
'''

#employee info class
class EmployeeInfo:
    #method that accepts the employee's id and name as arguments
    def __init__(self, idNum, name):
        #definition of data attributes
        self.idNum = idNum
        self.name = name
    def __str__(self):
        return ("Name: " + self.name)

#node in binary tree class
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

#insert function
def insert(root, node):
    if root == None:
        root = node
    else:
        #if current value is smaller than the root, adds to the left
        if root.data.idNum > node.data.idNum:
            if root.left == None:
                root.left = node
            else:
                insert(root.left, node)
        #if current node is bigger than the root, adds to the right
        elif root.data.idNum < node.data.idNum:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
#find function
def find(root, key):
    if root:
        if root.data.idNum == key:
            return root
        #if the key is smaller than the current node, checks the left child
        elif root.data.idNum > key:
            return find(root.left, key)
        #otherwise, checks the right child
        return find(root.right, key)
    else:
        return None

def main():

    #manually entered information
    root = Node(EmployeeInfo(2932,"Catelyn Stark"))
    insert(root, Node(EmployeeInfo(1034,"Cersei Lannister")))
    insert(root, Node(EmployeeInfo(3493,"Daenerys Targaryen")))
    insert(root, Node(EmployeeInfo(2293,"Jon Snow")))
    insert(root, Node(EmployeeInfo(2497,"Sansa Stark")))
    insert(root, Node(EmployeeInfo(5483,"Arya Stark")))
    insert(root, Node(EmployeeInfo(3994,"Tywin Lannister")))

    idNumber = int(input("Enter an ID to search: "))

    #calls find value function
    found = find(root, idNumber)

    #checks if the value is present
    if found:
        print(found.data)
    else:
        print("Employee is not found")

main()
