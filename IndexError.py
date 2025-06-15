try:
    sample_list = [10, 20, 30, 40]
    index = int(input(f"Enter an index (0 to {len(sample_list) - 1}): "))
    print("Element at index: ", sample_list[index])
except IndexError as e:
    print('IndexError caught: ', e)
except ValueError:
    print('Invalid Input! Please enter an integer.')