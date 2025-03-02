f = open("file1.txt", "r")
lines = f.readlines()
f.close()
longest = " "
for line in lines:
    if (len(line) > len(longest)):
        longest = line
print(longest)