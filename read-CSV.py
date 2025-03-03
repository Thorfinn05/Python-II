import csv

f = open("details.csv", "r")
read = csv.reader(f)
for row in read:
    print(row)