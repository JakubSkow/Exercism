"""Module verifying the amount of steps in Collatz Conjecture with provided number"""
def steps(number):
    """verifying the amount of steps in Collatz Conjecture with provided number"""
    
    #checking if number in positive
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    steps_amount = 0

    while (number != 1):
        if number % 2:
            number = number * 3 + 1
        else:
            number //= 2   
        steps_amount += 1

    return steps_amount