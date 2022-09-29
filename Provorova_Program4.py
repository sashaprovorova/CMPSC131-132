#base class
class assignment:
    
    #creates a method that accepts an assignmnet name anda list of grades as arguments
    def __init__(self, name, gradeList):

        #defines data attributes
        self.__asName=name
        self.__listGrades=gradeList 

    #creates mutator methods
    def set_name(self, name):
        self.__asName=name

    def set_number(self, gradeList):
        self.__listGrades=gradeList 
        
    #creates accesssor methods
    def get_name(self):
        return (self.__asName)

    def get_grades(self):
        return (self.__listGrades)


    #prints the grades stored in the list to the screen
    def print(self):
        grades=self.get_grades()
        #print("Grades unsorted: ", end="")
        for i in range (len(grades)):
            print(grades[i], end=" ")

    #sorts the elements in the list by using Bubble Sorting method
    def bubbleSort(self):
        dataset=self.get_grades()
        for i in range (len(dataset)-1,0,-1):
            for j in range (i):
                if dataset[j]>dataset[j+1]:
                    temp=dataset[j]
                    dataset[j]=dataset[j+1]
                    dataset[j+1]=temp
        
#main function
def main():
    
    #assignes the attributes
    givenName="Program 2" 
    givenList=[34, 67, 95, 12, 100, 78, 84, 53, 98, 90]

    #calls the main class
    request=assignment(givenName, givenList)

    #displays the grades
    print("Grades unsorted: ", end="")
    request.print()
    
    print(" ")
    print("Grades sorted: ", end="")

    #sorts and displays the grades
    request.bubbleSort()
    request.print()

main()

