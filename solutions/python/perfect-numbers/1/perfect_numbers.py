def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    index = number // 2
    dzielniki = 0

    while index >= 1:
        if number % index == 0:
            dzielniki += index
        index -= 1

    if dzielniki == number:
        return 'perfect'
    if dzielniki > number:
        return 'abundant'
    if dzielniki < number:
        return 'deficient'
