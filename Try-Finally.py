try:
    num = int(input('Enter a number to divide 100 by: '))
    result = 100 / num
    print('Result: ', result)
except ZeroDivisionError as e:
    print('ZeroDivisionError caught: ', e)
finally:
    print('This block runs anyway always - no matter what!')