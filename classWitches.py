
class newWitch:
    def __init__(self, userList):
        self.newList = userList

    def dispWitches(self):
        if not self.newList:
            print("List is empty")
        else:
            print('The witches available are as follows:')
            print("============================THE REPORT========================================= ")
            for witch in self.newList:
                witch.capitalize()
                print(witch)

    def checkWitch(self):
        if not self.newList:
            print("List is empty")
        else:
            for witch in self.newList:
                gCount = witch.count('g')
                gCount += witch.count('G')
                eCount = witch.count('e')
                eCount += witch.count('E')

                if gCount > eCount:
                    print(witch, " is a GOOD witch\n")
                elif gCount < eCount:
                    print(witch, " is an EVIL witch\n")
                elif gCount == eCount == 0 or gCount == eCount:
                    print(witch, " is a NEUTRAL witch\n")

    def updAddWitch(self,newAddName):#when using this parameter in our program we do not represent it as self cos it is gotten as object from another class within this same program
        if newAddName not in self.newList:
            self.newList.append(newAddName)
            print('The following name(s) will be added to the witch list: ', newAddName)

        else:
            print('The witch to be added already exists. please add another witch')
            print('Your witch has not been added to the list')

    def updateRemWitch(self,myExWitch): #it is gotten as an object of another class and referenced here. meaning somewhere in this program this is already self.something. check the customer class

        if myExWitch not in self.newList:
            print('The witch to be removed does not exist in the witch list. Please check the name and remove again')
            return 0
        else:
            self.newList.remove(myExWitch)
            print('Your witch has been removed from the list')
            return 1

    def singWitchCheck(self,singWitch):

        gCount = singWitch.count('g')
        gCount += singWitch.count('G')
        eCount = singWitch.count('e')
        eCount += singWitch.count('E')

        if gCount > eCount:
            print(singWitch, " is a GOOD witch\n")
        elif gCount < eCount:
            print(singWitch, " is an EVIL witch\n")
        elif gCount == eCount == 0 or gCount == eCount:
            print(singWitch, " is a NEUTRAL witch\n")


class userModule:
    def addWitch(self):
        print('please enter the name of the witch to add: ')
        self.userAdd = str(input())
        return self.userAdd
    def remWitch(self):
        print('Please enter the name of the witch to remove: ')
        self.userRem = str(input())
        return self.userRem
    def checkSingle(self):
        print('Please enter the name of the single witch to check: ')
        self.singWitch = str(input())
        return self.singWitch

witch = newWitch(['Esther', 'Olumide', 'Gregory'])
customer = userModule()

while True:
    print('please enter the desired option')
    print('press 1 to get information on witches')
    print('press 2 to add a witch to the list')
    print('press 3 to remove a witch from the list')
    print('press 4 to check good or bad witch in the list')
    print('press 5 to check a single witch entry')
    print('press 6 to quit')
    userIn = int(input())

    if userIn is 1:
        witch.dispWitches()
    elif userIn is 2:
        myNewWitch = customer.addWitch()
        myNewWitch = myNewWitch.capitalize()
        witch.updAddWitch(myNewWitch)

    elif userIn is 3:
        myExWitch = customer.remWitch()
        myExWitch = myExWitch.capitalize()
        witch.updateRemWitch(myExWitch)
    elif userIn is 4:
        witch.checkWitch()
    elif userIn is 5:
        singWitch = customer.checkSingle()
        witch.singWitchCheck(singWitch)
    elif userIn is 6:
        quit()

