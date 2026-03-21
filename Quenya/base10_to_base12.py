#!/usr/bin/venv python3
#
# Converts numbers given in base 10 to numbers in base 12

def base12_converter(x):
    """
    The integer x will be converted to base 12 with numbers 0 1 2 3 4 5 6 7 8 9 § $
    """
    # If = return 0
    if x == 0:
        return '0'
    # The remainders_list contains all the digits for the "new" number
    remainders_list = []
    while x != 0:
        if x % 12 == 10:
            remainders_list.append("§")
        elif x % 12 == 11:
            remainders_list.append("þ")
        else:
            remainders_list.append(str(x%12))
        x = x //12
    
    return ''.join(remainders_list[::-1])
