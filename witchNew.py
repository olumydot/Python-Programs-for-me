numberOfNames = int(input("Enter number of names you are interested in "))
names = []
countNames = 0

while countNames < numberOfNames:
    rawNames = input("Enter names ")
    names.append(rawNames)
    countNames += 1

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
        print(names[counter], " is an EVIL witch\n")
    elif gCount == eCount == 0 or gCount == eCount:
        print(names[counter], " is a NEUTRAL witch\n")