nums = range(1, 101)

def chickenMonkey(numbers):
    for num in numbers:
        if num % 5 == 0 and num % 7 == 0:
            print('ChickenMonkey')
        elif num % 5 == 0:
            print('Chicken')
        elif num % 7 == 0:
            print('Monkey')
        else:
            print(num)

chickenMonkey(nums)