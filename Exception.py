try:
    age = int(input('Enter your age: '))
    if(age < 0):
        raise Exception("Age can't be negative!")
    print("Your age: ", age)
except Exception as e:
    print("Exception caught: ", e)