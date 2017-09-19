import time
class Witches:
   names = [] #variable belonging to the class can be used within any method or function within that class

   def addNames(self,name): #has one arguement name
        self.names.append(name)
   def getNames(self):
        return self.names
   def display(self):
       # Name = Name[0].upper() + Name[1:]
       print(self.names)
obj = Witches() #after the class is created an object of the class is created
numberOfNames = int(input("Enter number of names: "))
for x in range(numberOfNames):
   Name = input("Enter Name %d: "%(x+1))
   Name = Name.lower()   #convert each letter to lower
   obj.addNames(Name)
print("============================THE REPORT========================================= ")
n = obj.getNames()
m = [x.capitalize() for x in n]
p = ', '.join(map(str,m))
print("NAMES: ",p)
print("------------------------------------------------------------------------------- ")
ecounter = 0
gcounter = 0
count = 1
for i in range(len(obj.getNames())):
    gcounter += obj.getNames()[i].count('g')
    ecounter += obj.getNames()[i].count('e')
    mm = obj.getNames()[i].capitalize()
    if gcounter>ecounter:
        print("(%d) %s contains %d \"e\" and %d \"g\" and thus, a GOOD witch: "%(count,mm,ecounter,gcounter))
    elif ecounter > gcounter:
        print("(%d) %s contains %d \"e\" and %d \"g\" and thus, an EVIL witch: " % (count,mm, ecounter, gcounter))
    else:
        print("(%d) %s contains %d \"e\" and %d \"g\" and thus, a NEUTRAL witch: " % (count,mm, ecounter, gcounter))
    # obj.getNames()[0].upper() + obj.getNames()[1:]
    ecounter = 0
    gcounter = 0
    count += 1
    time.sleep(0.5)




nameString = input("Enter different names separated by commas: ")
names = nameString.split(",")

print("\n")
counter = 0
for names[counter] in names:
    gCount = names[counter].count('g')
    gCount += names[counter].count('G')
    eCount = names[counter].count('e')
    eCount += names[counter].count('E')

    if gCount > eCount:
        print(names[counter], " is a GOOD witch\n")
    elif gCount < eCount:
        print(names[counter].lstrip(), " is an EVIL witch\n")
    elif gCount == eCount == 0 or gCount == eCount:
        print(names[counter].lstrip(), " is a NEUTRAL witch\n")


class newWitch:
    witchList = []

    def __init__(self, userWitchList):
        self.userWitchListed = userWitchList
        self.watchList = self.witchList.append(self.userWitchListed)

    def dispWitches(self):
        print('The witches available are as follows:')
        print("============================THE REPORT========================================= ")
        for witch in self.userWitchList:
            witch.capitalize()
            print(witch)
    def checkWitch(self):
        self.countNsmes = 0
        while self.countNsmes < len(self.watchList)



class userModule
    def addWitch(self):
        print('please enter the name of the witch to add: ')
        self.userAdd = str(input())
        return self.userAdd
    def remWitch(self):
        print('Please enter the name of the witch to remove: ')
        self.userRem = str(input())
        return self.userRem
