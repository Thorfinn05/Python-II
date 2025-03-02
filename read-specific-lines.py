f = open("file1.txt", "r")
lines = f.readlines()
f.close()
print(lines)
l = eval(input("Enter lines to read: "))
for i in l:
    print(lines[i], end = " ")