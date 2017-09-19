class Cards:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #class variable

    SUITS = ["c", "d", "h", "s"] #class variable

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

    #this class returns rep.. so when you print the class it shows whatever

class Hand: #lowercase "hand"  signifies an object of the class
    def __init__(self):
        self.cards = [] #create and empty list of objects from the class cards . Lowercase "cards" signifies an object of the class Cards

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "

        else:
            rep = "<empty>"

        return rep
    def clear(self):
        self.cards = []

    def add(self, card): #card= an object created from class Cards
        self.cards.append(card)

    def give(self, card, other):#other here is another object that was created from the hand class. This is another object of class hand
        self.cards.remove(card)
        other.add(card) #another object of the class "Hand" which has already been created calls the add module to take in the previous card given up



#inheritance
#all attributes of the class Hand gets inherited
#Hand is the base class
#Deck is the derived class
#deck inherits __init__, __str__, clear(), add() and give() methods
class Deck(Hand):
    def populate(self):
        for suit in Cards.SUITS: #this is how to declare class variable. class.variable
            for rank in Cards.RANKS:
                self.add(Cards(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards) #list proviously created and populated by every object of class Cards

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)

                else:
                    print("Can't continue deal. Out of cards!")
    def __str__(self):
        return "<unimaginable>"



#main
card1 = Cards("A", "c")
card2 = Cards("2", "c")
card3 = Cards("3", "c")
card4 = Cards("4", "c")
card5 = Cards("5", "c")


oldHand = Hand()
newHand = Hand()

oldHand.add(card1)
oldHand.add(card2)
oldHand.add(card3)
oldHand.add(card4)
oldHand.add(card5)

oldHand.give(card1,newHand) #give from the oldhand the card "card1" to the newHand object created
#in the newHand object of class "Hand" created the self.cards list is initiated. methods in the class are accesible

# print(oldHand) #this class does not return any values and thus will return an error when it tries to print

print(oldHand)
deck1 = Deck()
deck1.add(card5) #inherited the add from Hand class

print(deck1) #though it inherits the __str__ attributes from the Hand class, since it has its own then its own auto overrides that