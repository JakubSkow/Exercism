"""Program showing the prepare time for a lasagne"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(passed): 
    """check how much time is left for bake"""
    return EXPECTED_BAKE_TIME-passed

def preparation_time_in_minutes(number_of_layers): 
    """check how much time will take you to prepare depenting on number of layers"""
    return number_of_layers*2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): 
    """check how much time have you spend in the kitchen looking at how long lasagne is in the oven and how many layers you have prepared"""
    return number_of_layers*2+elapsed_bake_time
