f1 = open("file1.txt", "r")
data1 = f1.read()
f1.close()
f2 = open("file2.txt", "r")
data2 = f2.read()
f2.close()
f3 = open("file3.txt", "w")
f3.write(data1 + data2)
f3.close()