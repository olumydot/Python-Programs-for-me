import csv
from datetime import datetime
try:
    with open('testdata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='-')

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

# consider the following
path = "C:\\Users\\OluE\\Desktop\\Google Stock Market Data - google_stock_data.csv"
file = open(path)

for line in file:
    print(line)


lines = [line for line in file]

dataset = [line.strip().split() for line in file]


# I can rewrite all of this using csv

file = open(path, newline='')
reader = csv.reader(file)

# we know that the first line is the header
# we can read it using the next funtion

header = next(reader)
# the reader is a lazy iterator.. with the header we have taken off the first line

# data = [row for row in reader]  # reads the remaining data
# observe that the data is still read as strings .. now we make python read it appropriately

data = []
for row in reader:

    # row = [Date, Open, High, Low, Close, Volume, Adj.Close]
    # below i will parse the date.. this allows the date to become a flexible tool for me to use as I like..
    # what i have done in essence is to 'decompose' the date
    # or parse the data.. strptime= stringparsetime
    date = datetime.strptime(row[0], '%m/%d/%Y')
    # I can do more work on this date above and now rearrange as I like. I can scatter as i like since i already
    # parsed it in the statement above so its so flexible to use. strftime=stringformattime. eg
    # print(date.strftime('%Y__%b__:%d'))  # this will basically print the date as 2017__Dec__:07
    # note in the above that date is and must be a datetime object.. name doesnt matter. it could have been leg or cow
    open_price = float(row[1])  # this value is a float in
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = float(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])


print(data[1])

# to compute and store daily stock returns

return_path = "C:\\Users\\OluE\\Desktop\\Google Stock Market Data returns.csv"
# now I open this file in write mode
file_O = open(return_path, 'w')
# now a writer object
writer = csv.writer(file_O)
# I write the header first

writer.writerow(["Date", "Return"])


for i in range(len(data)-1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]
    daily_return = (todays_price - yesterdays_price)/yesterdays_price

    # I write the date format I intend to use thus:
    date_format = todays_date.strftime('%m/%d/%Y')
    # now I write this using the writer object
    writer.writerow([date_format, daily_return])