def is_isogram(string):
    string = ''.join(x for x in string if x.isalpha())
    
    seen = set()

    for letter in string.lower():
        if letter in seen:
            return False
        seen.add(letter)
    return True