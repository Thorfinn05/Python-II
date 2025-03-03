import csv

f = open("loginCredentials.csv", "w", newline="")
cwr = csv.writer(f)
cwr.writerow(['Username', 'Password'])
while True:
    username = eval(input("Enter username: "))
    password = eval(input("Enter password: "))
    cwr.writerow([username, password])
    ans = input('Enter y for more data: ')
    if(ans != 'y'):
        break
f.close()
f = open("loginCredentials.csv","r")
crd = csv.reader(f)
for data in crd:
    print(data)
f.close()