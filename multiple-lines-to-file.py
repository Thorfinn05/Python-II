def write_multiple_lines():
    with open("mylife.txt", "w") as file:
        print("Enter multiple lines (type 'STOP' to end):")
        while True:
            line = input()
            if line == "STOP":
                break
            file.write(line + "\n")
    print("File written successfully.")

write_multiple_lines()
