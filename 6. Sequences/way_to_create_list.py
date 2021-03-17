empty = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_number = sorted(numbers)
print(sorted_number)

digits = sorted("432985617")
print(digits)

#more_numbers = list(numbers)
#more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(more_numbers is numbers) #False then both are different lists
print(numbers == more_numbers)