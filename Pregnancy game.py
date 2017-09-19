print("Welcome to this new game")
name = input("what is your name:  ")
age = input("how old are you?:  ")
a = int(float(age))
country = input("What country are you from?:  ")
period = input("How many weeks ago was your last period:  ")
p = int(period)
first = input("Is this your first pregnancy:answer in CAPS?  ")
if first == "YES" and a >= 35:
    print("Welcome", name, ",Since your last period was", period, "weeks ago, you are most likely", 40-p , "weeks pregnant. Congratulations", name, "you are an elderly gravida 0")
elif first == "YES" and a < 35:
    print("Welcome", name, ",Since your last period was", period, "weeks ago, you are most likely", 40-p , "weeks pregnant. Congratulations", name, "you are a gravida 0")
else:
    print("Welcome", name, ",Since your last period was", period, "weeks ago, you are most likely", 40-p , "weeks pregnant. Congratulations", name, "your previous experience should make this easier for you. Go champ!")

input("\n\nPress ENTER to exit this program: ")
