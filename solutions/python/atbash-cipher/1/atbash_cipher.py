def encode(plain_text):
    plain_text = plain_text.lower()
    encoded = ''
    allChar = ord('z') + ord('a')

    for character in plain_text:
        if character.isalpha():
            encoded += chr(allChar - ord(character))
        elif character.isdigit():
            encoded += character


    chunk = []
    
    for i in range(0, len(encoded), 5):
        chunk.append(encoded[i:i+5])

    
    encoded = " ".join(chunk)
    
    

    return encoded
        
        


def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    decoded = ''
    allChar = ord('z') + ord('a')

    for character in ciphered_text:
        if character.isalpha():
            decoded += chr(allChar - ord(character))
        elif character.isdigit():
            decoded += character

    return decoded
