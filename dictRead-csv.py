import csv

f = open("cricket.csv", "r")
crd = csv.DictReader(f)
for row in crd:
    print(row)
f.close()