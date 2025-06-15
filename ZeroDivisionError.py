# try:
#     result = 10/0
# except ZeroDivisionError as e:
#     print('ZeroDivisionError caught:', e)


try: 
    a = int(input("Enter a number: "))
    num = int(input("Enter a number to divide " + str(a) + " by:"))
    result = a/num
    print("Result: ", result)
except ZeroDivisionError as e:
    print("ZeroDivisionError caught:", e)
except ValueError:
    print("Invalid input! Please enter an integer")