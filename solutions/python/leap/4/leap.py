"""Module verifying if provided year was a leap year"""
def leap_year(year):
    """function checking if provided year was a leap year"""
    
    if year % 4 != 0:
        return False
    
    if year % 100 != 0:
        return True
    
    return year % 400 == 0
