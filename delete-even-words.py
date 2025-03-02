f = open("file5.txt","r")
lines = f.readlines()
f.close()
f = open("file5.txt", "w")
for line in lines:
    words = line.split()
    new = " ".join(words[i] for i in range (len(words)) if i%2 == 0)
    f.write(new + "\n")
f.close()