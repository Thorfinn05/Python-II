f = open("first.txt", "r")
words = f.read().split()
f.close()
vowel = []
for word in words:
    if word[0] in "a e i o u":
        vowel.append(word)
with open("second.txt", "w") as file:
    file.write(" ".join(vowel))