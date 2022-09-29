class Car:
    
    #creates a method that accepts the car’s year model and make as arguments
    def __init__(self, yearModel, make):
        
        #defines data attributes
        self.__year__model=yearModel
        self.__make= make
        self.__speed=0
    
    #adds 5 to the speed data attribute
    def accelerate(self):
        self.__speed+=5

    #subtracts 5 from the speed data attribute
    def brake(self):
        self.__speed-=5

    #returns the current speed 
    def get_speed(self):
        return self.__speed
        
    
def main():

    #creates a Car object
    givenCar=Car('2021 CX-3', 'Mazda')

    #displays the current speed 
    print("Current speed of the car:", end=" ")
    
    #calls the accelerate method 5 times
    for i in range (5):
        givenCar.accelerate()
        currentSpeed=givenCar.get_speed()
        print(currentSpeed,end=" ")

    #calls the brake method 5 times    
    for j in range (5):
        givenCar.brake()
        currentSpeed=givenCar.get_speed()
        print(currentSpeed,end=" ")

main()


