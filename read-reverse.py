f = open("file4.txt", "r")
text = f.read().split()
f.close()
print(text[::-1])