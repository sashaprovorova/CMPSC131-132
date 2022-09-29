#base class
class PersonData:
    
    #creates a method that accepts all seven arguments
    def __init__(self,firstName,lastName, address, city, state, zipCode, phone):

        #defines data attributes
        self.__lname=lastName
        self.__fname=firstName
        self.__address=address
        self.__city=city
        self.__state=state
        self.__zip=zipCode
        self.__phone=phone

    #creates mutator methods
    def set_fname(self, firstName):
        self.__fname=firstName

    def set_lname(self, lastName):
        self.__lname=lastName
            
    def set_address(self, address):
        self.__address=address

    def set_city(self, city):
        self.__city=city

    def set_state(self, state):
        self.__state=state

    def set_zip(self, zipCode):
        self.__zip=zipCode

    def set_phone(self, phone):
        self.__phone=phone

    #creates accesssor methods
    def get_fname(self):
        return (self.__fname)

    def get_lname(self):
        return (self.__lname)
        
    def get_address(self):
        return (self.__address)

    def get_city(self):
        return (self.__city)

    def get_state(self):
        return (self.__state)

    def get_zip(self):
        return (self.__zip)

    def get_phone(self):
        return (self.__phone)

#derived class
class CustomerData(PersonData):
    
    #creates a method that accepts two arguments
    def __init__(self,firstName,lastName, address, city, state, zipCode, phone, customerNumber, mailingList):
        
        PersonData.__init__(self, firstName,lastName, address, city, state, zipCode, phone)

        #defines data attributes
        self.__mailingList=mailingList
        self.__customerNumber=customerNumber

    #creates mutator methods
    def set_mailingList(self, mailingList):
        self.__mailingList=mailingList
            
    def set_customerNumber(self, customerNumber):
        self.__customerNumber=customerNumber

    #creates accesssor methods
    def get_mailingList(self):
        return (self.__mailingList)
    
    def get_customerNumber(self):
        return (self.__customerNumber)
    
#main function
def main():
    import random
    #prompts the user to enter attributes
    
    #checks if the user entered a string
    try:
        givenFName=input("Enter the first name: ")
        givenLName=input("Enter the last nume: ")
        givenAddress=input("Enter the address: ")
        givenCity=input("Enter the name of the city: ")
        givenState=input("Enter the name of the state: ")
        customerNum=random.randint(0,100000)
        
    except ValueError:
        print('Invalid input, excpected a string.')
        
    #checks if the user entered the zip correctly
    answer1=True
    while answer1:
        try:
            givenZip=int(input("Enter the zip code: "))
            numInZip=len(str(givenZip))
            if numInZip!=5:
                raise ValueError
            else:
                answer1=False
        except ValueError:
            print('Invalid input, zip must contain 5 digits.')

    #checks if the user entered the phone number correctly
    answer2=True
    while answer2:
        try:
            givenPhoneNum=int(input("Enter the phone number: "))
            numInPhone=len(str(givenPhoneNum))
            if numInPhone!=10 and numInPhone!=11:
                raise ValueError
            else:
                answer2=False
        except ValueError:
            print('Invalid input, phone number must contain 10/11 digits.')
            
    #checks if the user entered True/False string and converts it into boolean 
    answer3=True
    
    while answer3:
        try:
            givenmailingList=input("Enter \"True\" or \"False\" depending on whether or not the customer wishes to be on a mailing list: ")
            if givenmailingList!=("True") and givenmailingList!=("False"):
                raise ValueError
            elif givenmailingList==("True"):
                givenmailingList=bool("True")
                answer3=False
            elif givenmailingList==("False"):
                givenmailingList=bool("")
                answer3=False
        except ValueError:
            print('Invalid input, excpected a boolean')

    #creates an object of the CustomerData class

    givenPerson=CustomerData(givenFName,givenLName,givenAddress, givenCity, givenState, givenZip,givenPhoneNum,customerNum,givenmailingList)

    #displays the data to the user
    print(" ")
    print("Customer's first name: ", givenPerson.get_fname())
    print("Customer's last name: ", givenPerson.get_lname())
    print("Address: ",givenPerson.get_address())
    print("City: ", givenPerson.get_city())
    print("State: ", givenPerson.get_state())
    
    print("Zip: ", givenPerson.get_zip())
    print("Phone: ", givenPerson.get_phone())
 
    print("Unique number: ",givenPerson.get_customerNumber())
    print("Customer is on a mailing list: ", givenPerson.get_mailingList())
    
   
main()
