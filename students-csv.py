import csv

f = open("students.csv","w",newline="")
cwr = csv.writer(f)
cwr.writerow(['Roll', 'Name', 'Score', 'Class'])
cwr.writerow([101, 'Alex', 80, 12])
cwr.writerow([102, 'Monica', 84, 12])
cwr.writerow([103, 'Ajay', 72, 12])
cwr.writerow([104, 'Irfan', 82, 11])
f.close()

f = open("students.csv","r")
crd = csv.reader(f)
def count_rec(crd):
    c = 0
    for data in crd:
        if(data['Score'] > '80'):
            print(data)
            c += 1
    return c
print("Number of records > 80 is: ", count_rec(crd))
f.close()