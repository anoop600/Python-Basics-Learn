def sum_eo(number, condition):
    sum = 0
    if condition == 'e':
        for number in range(2, number, 2):
            sum += number
    elif condition == 'o':
        for number in range(1, number, 2):
            sum += number
    else:
        sum = -1
    return sum
    
print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))