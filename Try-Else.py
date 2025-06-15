try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
except ValueError:
    print("ValueError: Not an valid integer !")
else:
    print("Conversation successful, number is: ", number)