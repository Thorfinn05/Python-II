f = open("file1.txt", "r")
words = f.read().split()
f.close()
longest = " "
for word in words:
    if (len(word) > len(longest)):
        longest = word
print(longest)