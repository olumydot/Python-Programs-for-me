class Employee:

    numberOfHoursWorked = 5 #this is a class attribute/variable

    def targetMet(self):
        if self.numberOfHoursWorked == 5:
            print("Target hours met")
        elif self.numberOfHoursWorked < 5:
            print(self.name, 'you have not met the required Hours')
        else:
            print(self.name, 'you have worked overtime')

employeeOne = Employee()
employeeOne.name = 'Mike' #creates an instance attribute name. it will not reflect in other instances
print(employeeOne.name)

Employee.name = 'Michael' #create a class attribute that reflects in all classes
print(employeeOne.name)

employeeOne.numberOfHoursWorked = 15
print(employeeOne.targetMet())
employeeTwo = Employee()

employeeTwo.name = 'Dara'
print(employeeTwo.name)

employeeTwo.numberOfHoursWorked = 3

print(employeeTwo.targetMet())

#
# class Witches:
#     #managerNameList = []
#     #storeLocationList = []
#     #storeDictionary = {}
#     #storeNumberList = []
#     #self.storeEmployeeNumber = storeEmployeeNumber
#     #self.storeLocation = storeLocation
#     #self.storeNumber = storeNumber
#     #self.storeManager = storeManagerName
#     # def __init__(self, storeHealth = 'Good'):
#     #     self.storeHealth = storeHealth
#     # def __init__(self, counter=0,:
#     #
#     #     self.names = names
#     def addWitchNumber(self):
#         self.nameString = input("Enter different names separated by commas: ")
#         self.names = self.nameString.split(",")
#     def countWitches(self):
#
#         self.counter = 0
#         for self.name[self.counter] in self.names:
#             self.gCount = self.names[self.counter].count('g')
#             self.gCount += self.names[self.counter].count('G')
#             self.eCount = self.names[self.counter].count('e')
#             self.eCount += self.names[self.counter].count('E')
#
#     def processesResult(self):
#         if self.gCount > self.eCount:
#             print(self.names[self.counter], " is a GOOD witch\n")
#         elif self.gCount < self.eCount:
#             print(self.names[counter].lstrip(), " is an EVIL witch\n")
#         elif self.gCount == self.eCount == 0 or self.gCount == self.eCount:
#             print(self.names[self.counter].lstrip(), " is a NEUTRAL witch\n")
#
# #
# # durhamStore = joannStores()
# # durhamStore.addStoreNumber(2)
# # durhamStore.addStoreNumber(2)
# # durhamStore.addStoreNumber(2)
# # durhamStore.addStoreNumber(2)
# # print(durhamStore.getStoreNumber())
# #
#
# newWitch = Witches()
# def main():
#     newWitch.addWitchNumber()
#     newWitch.countWitches()
#     newWitch.processesResult()
#
#     input("press Enter to exit his program")
#
# main()


class Employer:
    def employeeDetails(self): #self meant the object instance of the class
        self.name = input("What is your name?:  ") #this is creation of the object attribute name as mike. self is the instance of the object created
        #self allows name attribute to be accesible to other methods. the attribute is accesible to other methods
        # pass #means dont do anything

    @staticmethod
    def showWelcomeMessage():
        #this program doesnt make use of any attribute whether class or instance.. thus we do not need the self arguement or parameter
        #thus we use a special decorator @staticmethod. this extends the functionality of the method since we are not using self
        print("You are welcome to this program")
employee = Employer() #new instance of the class Employer is created and that is the 'self'..
#so for example in the method employeeDetails when we say self.name = .. it means we set the attribute name to the input given by the user
employee.employeeDetails()
employee.showWelcomeMessage()