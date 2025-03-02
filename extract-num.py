f = open("file4.txt", "r")
text = f.read()
f.close()
num = []
for word in text.split():
    if word .isdigit():
        num.append(word)
print(num)