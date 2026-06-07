"""Module to verify if provided numer is Armstrong Number"""

def is_armstrong_number(number):
    #Changing the number into the table and checking how long it is
    digits = [int(place) for place in str(number)]
    length = len(digits)

    #creating a variable that will be used to check the sum of the digits
    result=0

    #adding the digit^ <length of the number>
    for digit in digits:
        result+=digit**length

    #sending the True/False bool of the number was a Armstrong Number
    return result==number