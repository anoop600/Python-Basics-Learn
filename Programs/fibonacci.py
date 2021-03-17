#number is sum of 2 previous numbers

def fibonacci(number , accumulator={}):
    accumulator[0] = 0
    accumulator[1] = 1
    
    if (0 <= number <= 1 or accumulator.get(number)):
        return accumulator[number]

    accumulator[number] = fibonacci(number-1, accumulator)+fibonacci(number-2, accumulator)
    return accumulator[number]

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))


#0,1,1,2,3,5,8,13,21