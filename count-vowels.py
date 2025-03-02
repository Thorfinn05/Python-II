f = open("second.txt", "r")
words = f.read().split()
f.close()
vowels = 0
for word in words:
    if word[0] in "aeiouAEIOU":
        vowels += 1
print(vowels)