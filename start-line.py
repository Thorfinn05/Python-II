f = open("diary.txt", "r")
lines = f.readlines()
f.close()
for line in lines:
    if line.startswith("P"):
        print(line, end=" ")