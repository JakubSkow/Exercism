def encode(numbers):
    result = []
    for number in numbers:
        parts = []
        if number == 0:
            parts.append(number & 0x7F)
        while number > 0:
            parts.append(number & 0x7F)
            number >>= 7
        parts.reverse()
        for part in range(len(parts)-1):
            parts[part] |= 0x80
        result+=parts
    return result

def decode(bytes_):
    number = 0
    result = []
    
    
    for byte in bytes_:
        data = byte & 0x7F
        number = (number << 7) + data
        if not(byte & 0x80):
            result.append(number)
            number = 0

    if result == []:
        raise ValueError("incomplete sequence")
    return result
