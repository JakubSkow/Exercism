def is_valid(isbn):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False
            
    isbn = isbn.upper()
    isbn = ''.join(x for x in isbn if x.isdigit() or x == 'X')

    if len(isbn) != 10:
        return False

    if 'X' in isbn[:-1]:
        return False

    character = 10
    
    total = 0
    
    for number in isbn:
        if number == 'X':
            value = 10
        else:
            value = int(number)

        total += (value * character)
        character -= 1

    return total % 11 == 0
