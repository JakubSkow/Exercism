def is_armstrong_number(number):
    pass

    digits = [int(x) for x in str(number)]
    length = len(str(number))
    
    result=0
    
    for i in range(len(digits)):
        result+=digits[i]**length
    
    if result==number:
        return True
    else:
        return False