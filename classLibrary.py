#if you put anything beside self in a bracket, that stuff is
#1. either a initial parameter which is important for an instance of the object
#for example here: what is a library without a list of books. The init means it is initialized
#meaning the user can initialize by providing this when the object of the library is initiated.
#this parameter must be filled. now the parameter beside self will always be provided either by the user or from within the program
#2. if its not initialized parameter beside self then it is gotten from some other place within the program.
#when using such within your program you do not have to use the self.attribute name in using such if you are not originally creating the instance
class Library:
    def __init__(self, listOfBooks): #the init will initialize first. the listOfBooks will be provided by the user. If there was a print statement in this init it will print first. method is not called for this to be executed
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available books: ")

        for book in self.availableBooks:
            print(book)

    def lendABook(self, requestedBook): #we see 'requestedBook' is provided from another part of the program as an input to this part of the program. it was created as an instantiation of an object
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("The book is not available in out list")

    def addABook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("you have returned the book. Thank you!")

    def updateLibrary(self, userbookUpdate):
        self.availableBooks.append(userbookUpdate)


class Customer:
    def requestBook(self):
        print("Enter a book you will like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you are returning")
        self.book = input()
        return self.book


library = Library(['me and you', 'you and me', 'not you and me'])
customer = Customer()
while True:
    print("Enter 1 to display available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Press 4 to update the library (Option is for librarian only:")
    print("Enter 5 to exit")
    userChoice = int(input())

    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendABook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        if returnedBook not in library.availableBooks:
            library.addABook(returnedBook)
        else:
            print("you cannot return a book already in the Library. See the librarian")
    elif userChoice is 4:
        print("please enter the books you want to add to the library: ")
        userUpdate = str(input())
        for x in userUpdate:
            library.updateLibrary(x)
    elif userChoice is 5:
        quit()



