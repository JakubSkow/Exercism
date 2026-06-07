"""Module checking the amount of grains of wheat taht are doubled on each square"""

def square(number):
    #checking the amount on specific square
    if 1 <= number <= 64:
        return 2**(number-1)
    raise ValueError("square must be between 1 and 64")


def total():
    #listing the total amount of grains on the board
    return 2**64-1
