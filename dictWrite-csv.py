import csv

f = open("cricket.csv","a",newline="")
cwr = csv.DictWriter(f, fieldnames=['Country','Played','Won','Lost','Tie','No Result'])
while True:
    content = eval(input("Enter row: "))  #{"Country":"Pakistan","Played":"745","Won":"380","Lost":"335","Tie":"7","No Result":"23"}
    cwr.writerow(content)
    ans = input("Enter y for more rows: ")
    if (ans != 'y'):
        break
f.close()