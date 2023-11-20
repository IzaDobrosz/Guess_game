import random


def guess(number):

    user_number = int(input("Guess the number: "))

    while user_number != number:
        if user_number < number:
            print('Too small!')
        elif user_number > number:
            print('Too big!')
        user_number = int(input("Guess the number: "))
    print('You won!')

number = random.randint(1, 4)


result = guess(number)
print(result)
