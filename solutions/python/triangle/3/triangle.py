"""Module checking if triangle is equilateral, isosceles, or scalene"""
def is_triangle(a, b, c):
    #checking if this is even triangle by checing the lenght of all sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b >= c and b + c >= a and a + c >= b


def equilateral(sides):
    #checking if all sides are even

    if not is_triangle(sides[0], sides[1], sides[2]):
        return False
    
    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    #checking if only two sides are the same (can be two or more, but should be additional part checking if all sides are even and returning false if so)
    if not is_triangle(sides[0], sides[1], sides[2]):
        return False
    
    return (
        sides[0] == sides[1] or
        sides[0] == sides[2] or
        sides[1] == sides[2]
    )


def scalene(sides):
    #checking if all sides are different
    if not is_triangle(sides[0], sides[1], sides[2]):
        return False
    
    if not sides[0] == sides[1] and not sides[0] == sides[2] and not sides[1] == sides[2]:
        return True

    return False
