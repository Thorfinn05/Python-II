import csv

f = open("details.csv", "r")
read = csv.reader(f)
next(read)
for row in read:
    print(row)