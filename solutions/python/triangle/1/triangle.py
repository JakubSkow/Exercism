"""Module checking if triangle is equilateral, isosceles, or scalene"""
def isTriangle(a, b, c):
    #checking if this is even triangle by checing the lenght of all sides
    if a and b and c:
        if a + b >= c and b + c >= a and a + c >= b:
            if a <= 0 and b <= 0 and c <= 0:
                return False
            else: 
                return True
    else:
        return False



def equilateral(sides):
    #checking if all sides are even

    if not isTriangle(sides[0], sides[1], sides[2]):
        return False
    
    if sides[0] == sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    #checking if only two sides are the same (can be two or more, but should be additional part checking if all sides are even and returning false if so)
    if not isTriangle(sides[0], sides[1], sides[2]):
        return False
    
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    return False
    

def scalene(sides):
    #checking if all sides are different
    if not isTriangle(sides[0], sides[1], sides[2]):
        return False
    
    if not sides[0] == sides[1] and not sides[0] == sides[2] and not sides[1] == sides[2]:
        return True

    return False
