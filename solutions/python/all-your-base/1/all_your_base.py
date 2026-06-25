def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    total = 0

    for digit in digits:
        total = total * input_base + digit

    if total == 0:
        return [0]
    
    final =[]

    while total > 0:
        remainder = total % output_base
        final.append(remainder)
        total //= output_base

    return final[::-1]