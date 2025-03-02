f = open("INDIA.TXT", "r")
text = f.read().lower()
f.close()
count = 0
for word in text.split():
    if word == "india":
        count += 1
print(count)