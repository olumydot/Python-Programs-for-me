import csv
try:
    with open('testdata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = '-')

        voltages = []
        time = []

        for row in readCSV:
            print(row)
            #time.append(row)

        print("\n")
        print(voltages)
    print("\n")
    print(time)
except IndexError:
    print("IndexError")
except ValueError:
    print("ValueError")