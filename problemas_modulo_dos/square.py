import math


def is_square(n):
    # if n < 0:
    #     b = False
    # else:
    #     b = math.sqrt(n).is_integer()
    # return b
    return math.sqrt(n).is_integer() if n > 0 else False


assert is_square(-1) == False
assert is_square(25) == True
assert is_square(26) == False
assert is_square(4) == True
assert is_square(37) == False