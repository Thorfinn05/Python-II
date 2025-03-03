import csv

new_data = [
    ["Country","Played","Won","Lost","Tie","No Result"],
    ["England",746,375,334,9,28],
    ["Australia",949,575,331,9,34],
    ["India","987","513","424","9","41"]
]

f = open("cricket.csv", "w", newline="")
cwr = csv.writer(f)
cwr.writerows(new_data)
f.close()

f = open("cricket.csv","r")
crd = csv.reader(f)
for row in crd:
    print(row)
f.close()

f = open("cricket.csv","a",newline="")
cap = csv.writer(f)
cap.writerow(["New Zealand",742,345,347,11,30])
f.close()

