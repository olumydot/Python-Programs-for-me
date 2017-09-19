from witchesClass import Witches
maxLength = int(input("Please enter the number of data to be added to created list: "))
dataList =[]

for x in range(maxLength):
    inputRawData = str(input("Please enter the name of the witch: "))
    inputRawData = inputRawData.lower()
    dataList.append(inputRawData)
print("\n")
count = 0
limit = len(dataList)-1
while count <= limit:
    for dataList[count] in dataList:

        count1 = 0
        count2 = 0

        for char in dataList[count]:
            if char == 'g':
                count1 += 1
            elif char == 'e':
                count2 += 1

        if count1 > count2:
            print(dataList[count], " is a GOOD witch\n")
        elif count2 > count1:
            print(dataList[count], " is an EVIL witch\n")
        elif count2 == count1 == 0 or count1 == count2:
            print(dataList[count], " is a NEUTRAL witch\n")

        count += 1
