def rows(letter):
    letter = letter.upper()
    howMany = ord(letter) - ord('A') + 1

    rows = howMany * 2 - 1

    inner = 0
    character = 'A'

    result = []


    for row in range(howMany):
        left = ord(letter) - ord(character)   

        if row == 0:
            result.append(" " * left + character + " " * left)
        else:
            result.append(" " * left + character + " " * inner + character + " " * left)
        inner = inner + 1 if inner == 0 else inner + 2
        character = chr(ord(character) + 1)
    result += list(reversed(result[:-1]))
    return result