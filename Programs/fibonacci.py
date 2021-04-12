# number is sum of 2 previous numbers
def validate_data_type(number):
    if type(number) is str:
        raise ValueError("Error. value must be number, not a string")
    elif number < 0:
        raise ValueError(
            "Error. Invalid number passed. Number must be positive")
    else:
        return True


def fibonacci(number, accumulator={}):
    """[Return `n`th fibonacci number from the series. 
    Used recurssive programming and made it efficient using dynamic programming.
    Used accumulator to store intermediate vaules generated, which reduces time complexity.
    Sharing already computed data with each function call.]

    Args:
        number ([type]): [description]
        accumulator (dict, optional): [description]. Defaults to {}.

    Returns:
        [int]: [`n`th fibonacci number]
    """
    if(validate_data_type(number)):
        accumulator[0] = 0
        accumulator[1] = 1
        if (0 <= number <= 1 or accumulator.get(number)):
            return accumulator[number]
        accumulator[number] = fibonacci(
            number-1, accumulator) + fibonacci(number-2, accumulator)
        print(accumulator)
        return accumulator[number]


# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))
# print(fibonacci(8))
# print(fibonacci(50))
print(fibonacci('a'))

# 0,1,1,2,3,5,8,13,21
