f = open("file1.txt", "r")
words = f.read().split()
f.close()
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
f = open("file1.txt", "w")
f.write(" ".join(unique))
f.close()