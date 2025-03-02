file = open ("file1.txt", "r")
data = file.read()
words = data.split()
print("Content: \n", data)
count = 0

d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

unique = list + (d.keys())
for i in range(len(unique)):
    for j in range(i+1, len(unique)):
        word1 = unique[i].lower()
        word2 = unique[j].lower()
        if(len(word1) == len(word2)):
            if(sorted(word1) == sorted(word2)):
                count += 1

print("No. of anagrams in file: ", count)
file.close()
