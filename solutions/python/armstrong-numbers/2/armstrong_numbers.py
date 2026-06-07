def is_armstrong_number(number):
    pass

    digits = [int(place) for place in str(number)]
    length = len(str(number))
    
    result=0
    
    for place in range(len(digits)):
        result+=digits[place]**length
    
    if result==number:
        return True
    else:
        return False