f = open("file.txt", "w")
print("Enter multiple lines: ")
while True:
    line = input()
    if line == "END":
        break
    f.write(line + "\n")
f.close()