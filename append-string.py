text = input("Enter text: ")
f = open("file2.txt", "a")
f.write(text + "\n")
f.close()