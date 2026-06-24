def rotate(text, key):
    result = ""

    for character in text:
        if character.isalpha():
            if character.islower():
                start = ord("a")
            else:
                start = ord("A")

            shifted = (ord(character) - start + key) % 26
            result += chr(start + shifted)

        else:
            result += character

    return result
