def commands(binary_str):
    result = []

    if int(binary_str[4]):
        result.append('wink')
    if int(binary_str[3]):
        result.append('double blink')
    if int(binary_str[2]):
        result.append('close your eyes')
    if int(binary_str[1]):
        result.append('jump')
    if int(binary_str[0]):
        result=list(reversed(result))

    return result
        