def sum_numbers(*numbers: float) -> float:
    """Fund the sum of numbers passed to the sum_numbers function

    Returns:
        float: [description]
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum

def sum_numbers_builtin(*numbers: float) -> float:
    """Fund the sum of numbers passed to the sum_numbers function

    Returns:
        float: [description]
    """
    return sum(numbers)


print(sum_numbers(1,2,3))
print(sum_numbers_builtin(12.5 , 3.147, 98.1))