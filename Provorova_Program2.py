#base class
class Employee:

    #creates a method that accepts the employee's name and number as arguments
    def __init__(self, name, number):

        #defines data attributes
        self.__employeeName=name
        self.__employeeNumber=number

    #creates mutator methods
    def set_name(self, name):
        self.__employeeName=name

    def set_number(self, number):
        self.__employeeNumber=number
        
    #creates accesssor methods
    def get_name(self):
        return (self.__employeeName)

    def get_number(self):
        return (self.__employeeNumber)
        
#derived class
class ProductionWorker(Employee):

    #creates a method that accepts the employee's name, number, shift number and pay rate as arguments
    def __init__(self, name, number, shiftNum, payRate):
        
        Employee.__init__(self, name, number)

        #defines data attributes
        if shiftNum==1 or shiftNum==2:
            self.__shiftNumber=shiftNum
        else:
            print("ERROR")
            
        self.__hourlyPay=payRate

    #creates mutator methods
    def set_shift_num(self, shiftNum):
        if shiftNum==1 or shiftNum==2:
            self.__shiftNumber=shiftNum
        else:
            print("ERROR")

    def set_hourly_payrate(self, payRate):
        self.__hourlyPay=payRate

    #creates accesssor methods
    def get_shift(self):
        if self.__shiftNumber==1:
            return "Day shift"
        elif self.__shiftNumber==2:
            return "Night shift"

    def get_payrate(self):
        return (self.__hourlyPay)

#main function
def main():

    #prompts the user to enter attributes
    employeeName=input("Enter employee's name: ")
    employeeNumber=int(input("Enter employee's number: "))
    employeeShift=int(input("Enter the shift number: "))
    employeePay=float(input("Enter the hourly pay rate: "))
    
    #creates an object of the ProductionWorker class
    givenEmployee=ProductionWorker(employeeName,employeeNumber, employeeShift, employeePay)

    #displays the data to the user
    print(" ")
    print("Employee's name: ", givenEmployee.get_name())
    print("Number: ",givenEmployee.get_number())
    print("Shift: ", givenEmployee.get_shift())
    print("Hourly pay: $", givenEmployee.get_payrate())

main()

