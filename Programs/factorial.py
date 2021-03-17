def factorial(number , accumulator=1):
    if number == 1:
        return accumulator
    return factorial(number - 1, number*accumulator)

print(factorial(5))