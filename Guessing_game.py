import random

random_no = random.randint(1, 1000)
player = int(input("Guess a number between 1 and 1000:   "))
trials = 1
while player != random_no:

    if player > random_no:
        print("guess lower")

    else:
        print("guess higher")

    player = int(input("Guess a number between 1 and 1000 or press enter to exit this game"))
    trials += 1

print("you guessed correctly after {} trials".format(trials))


#another way to write this and make it more interactive.

import random

random_no = random.randint(1, 1000) #generates a single random integer between 1 and 1000
player = int(input("Guess a number between 1 and 1000:  ")) #ask the player to guess
trials = 1
while player != random_no: #as long as the player has not guessed correctly, execute the following

    if player > random_no: #if this condition is true, execute the next line by asking player to guess lower in the next line and then loops back to the beginning of the loop
        #note that if the above is satisfied, the else is not checked at all. The program takes the new value of player
        #and checks at the while condition to see if its fulfilled
        player = int(input("Guess a number between 1 and 1000 again. This time guess lower than previous:  ")) #this stores a new variable for player
        #and the
    else: #if the above is not satisfies
        player = int(input("Guess a number between 1 and 1000. Guess higher this time:  "))

    trials += 1

print("you guessed correctly after", trials , "trials")



#on the use of random

import random

word = input("Please enter your favorite word")

print("The word is ", word, "\n")
upper = len(word)
lower = -len(word)

for i in range(50):
    position = random.randrange(lower,upper)
    print("word[", position, "]\t" , word[position])

input("Press the enter key to exit. ")


#create new strings

message = input("Enter a message")
message = message.strip()
new_message = ""
vowels = "aeiou"

for letter in message:
    if letter.lower() not in vowels:
        new_message += letter
        print("A new string has been created: ", new_message) #if i take this line out, the step by step removal of the vowels is not seen

print("your message without vowels is: ", new_message)