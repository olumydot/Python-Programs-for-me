import time
class Car:
    #the following variables or attributes belong to every instance of the class Car that will be created
    tyres = 4
    door = 4
    def __init__(self,color= str(input('What is the color or the Car: ')),type = str(input("What type of car is it? ")), VIN = input("please enter the vehicle 5-digit VIN")):
        print("This is a program to demonstrate how classes work")
        time.sleep(2)
        self.color = color
        self.type = type
        self.vin = VIN
        if not (VIN.isdigit() and int(VIN) <= 99999):
            raise ValueError("VIN can only be numeric values and the digits not more than 5")

        # if len(VIN) is not 5:
        #     raise ValueError("The length cannot be greater than 5 digits")


    def getCarInfo(self):
        print()
        print('The information of the vehicle is as follows:')
        time.sleep(1)
        print('This is a car with', self.door, 'doors')
        time.sleep(1)
        print('The car has', self.tyres, 'tyres')
        time.sleep(1)
        print('The color of the car is', self.color)
        time.sleep(1)
        print('It is a type', self.type, 'car')
        time.sleep(1)
        print('The VIN of the car is as follows: ', self.vin)
        time.sleep(1)

    def moveCarForward(self):
        self.decision = input('Do you want to move car forward? ')
        self.time = int(input('How long do you want the car to move forward in seconds please: '))
        self.decision = self.decision.lower()

        if self.decision is 'yes' or 'y' or 'yea':
            print("This car is moving forward")
            time.sleep(self.time)
            return "moving"
        else:
            pass
    def reverseCar(self):
        self.back = input('Do you want to move car backwards?:')
        self.time1 = int(input('How long do you want the car to reverse in seconds please: '))
        self.back = self.back.lower()

        if self.back is 'yes' or 'y' or 'yea':
            print("This car is moving forward")
            time.sleep(self.timeer)
            return 'reverse'
        else:
            pass

    def cruzeCar(self):
        self.cruzeSpeed = int(input("Please enter cruze speed"))
        print(self.cruzeSpeed, 'is the cruise speed')
        return self.cruzeSpeed

    def checkCruzeSafeSpeed(self, cruzespeedset): #cruzespeedset was provided as a returned value of an instantiated object in one of the mthods
        self.inputLimit = int(input('What is the Limit of the area'))
        if cruzespeedset > self.inputLimit:
            print('slow down. you are moving too fast')
        elif cruzespeedset <= self.inputLimit:
            print('your speed is good')

benz = Car()

while True:
    print('please enter the desired option')
    print('press 1 to get information on the class')
    print('press 2 to move car forward')
    print('press 3 to reverse car')
    print('press 4 to set cruise speed')
    print('press 5 to check cruize safety level')
    print('press 6 to quit')
    userIn = int(input())

    if userIn is 1:
        benz.getCarInfo()
    elif userIn is 2:
        benz.moveCarForward()
    elif userIn is 3:
        benz.reverseCar()
    elif userIn is 4:
        cruzespeedset = benz.cruzeCar()
    elif userIn is 5:
        try:
            benz.checkCruzeSafeSpeed(cruzespeedset)
        except NameError:
            print("Set the Cruise speed first using the option 4")
    elif userIn is 6:
        quit()

