""""
Begin by creating an implementation of a linked list using your own code or
the code presented in the lesson on Linked Lists. Make sure the linked list
is capable of inserting, deleting, and searching the list.

Next write a program which asks the user to enter 10 assignment grades.
Store those grades in a linked list. Next output the grades and their average
to the screen.
"""

#base class "Node"
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
    
#base class "LinkedList"   
class LinkedList:
    
    #creates a method that accepts the head of the list as an argument
    def __init__(self, head=None):
        self.head=head
        
    #creates an insert method 
    def insert(self, data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node

    #creates a size method
    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.get_next()
        return count

    #creates a search method
    def search(slef, data):
        current=self.data
        found=False
        while current and found is False:
            if current.get_data()==data:
                found=True
            else:
                current=current.get_next()
        if current is None:
            raise ValueError("Data are not in the list")
        return current

    #creates a delete method
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    #prints the grades stored in the list to the screen
    def print(self):
        temp=self.head
        while temp != None:
            print(temp.data, end=" " )
            temp=temp.next
        
    #calculates the average 
    def  average(self):
        temp=self.head
        sum=0
        count=0
        while temp != None:
            sum+=temp.data
            count+=1
            temp=temp.next
            
        return (sum/count)

        
#main function
def main():
    
    #calls the list method
    givenGrades=LinkedList()
    
    #requests the information from the user
    print("Enter 10 assignment gardes: " )
    for i in range (10):
        givenGrades.insert(int(input()))
        
    #displays the grades
    print("Grades: ")
    givenGrades.print()
    
    #displays the average
    print(" ")
    averageGrade=givenGrades.average()
    print("Average: ", round(averageGrade))
    
main()
        
