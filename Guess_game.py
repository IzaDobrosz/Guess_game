import random


def guess(number):

    while True:

        try:
            user_number = int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")
            continue

        if user_number < number:
            print('Too small!')
        elif user_number > number:
            print('Too big!')
        else:
            print('You won!')
            break


drawn_number = random.randint(1, 100)

guess(drawn_number)
