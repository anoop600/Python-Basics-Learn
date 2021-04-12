def fibonacci(number):
    """Fibonacci using for loop

    Args:
        number ([int]): [`n` th fibonacci number to be find]

    Returns:
        [int]: [return `n` th fibonacci number]
    """
    if 0 <= number <= 1:
        return number

    first, second = 0,1

    result = None
    for f in range(number-1):
        result = first + second
        first = second
        second = result
    return result

for i in range(36):
    print(i, fibonacci(i))
