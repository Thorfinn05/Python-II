class CustomError (Exception):
    pass
try:
    text = input("Type 'hello' to continue: ")
    if text.lower() != 'hello':
        raise CustomError("You didn't type 'hello'!")
    print("Thanks! You followed rule.")
except CustomError as e:
    print("CustomError caught: ", e)