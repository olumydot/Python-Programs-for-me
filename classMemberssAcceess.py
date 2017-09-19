#public => memberName
#protected => _memberName
#private => __memberName

class Car:
    numberOfWheels = 4 #accesible anywhere within the program
    _color = 'Black' #can be accessed within the class and within its derived classes. also outside of the classes
    __yearOfManufacture = 2017 #cannot be accessed outside the class


class BMW(Car):
    def __init__(self):
        print(" The color of the car is: ", self._color)

car = Car()
print("Public attribute: numberOfWheels: ", car.numberOfWheels)
#print("Private attribute: yearOfManufacture:", car.__yearOfManufacture)
#the proper way to aceess such private attribute is below
print("Private attribute: yearOfManufacture:", car._Car__yearOfManufacture)

bm = BMW()
