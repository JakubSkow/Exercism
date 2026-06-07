def is_armstrong_number(number):
    pass

    digits = [int(place) for place in str(number)]
    length = len(digits)
    
    result=0
    
    for digit in digits:
        result+=digit**length
    
    return result==number