with open("file.txt","w") as file:
    i = 1
    while(i==1):
        c=int(input('Enter choice(0/1): '))
        if(c==0):
            i=2
        else:
            l=input("Enter elements: ")
            file.writelines(l+"\n")

with open("file.txt","r") as file:
    a = file.readlines()

with open("file1.txt","w") as file:
    file.writelines(a)