f = open("file2.txt", "r")
words = f.read().split()
f.close()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)