f = open("file1.txt", "r")
lines = f.readlines()
f.close()
f = open("file1.txt", "w")
l = eval(input("Enter lines to skip: "))
i = 0
for line in lines:
    if i not in l:
        f.write(line)
    i += 1
# data = f.readlines()
# print(data)
f.close()