even = [2,4,6,8]
odd = [1,3,5,7,9]

print(min(even))
print(min(odd))

print()

print(max(even))
print(max(odd))

print()

print(len(even))
print(len(odd))

print()

print("anoop".count("oo"))

empty_list = []
numbers = even + odd
print(numbers)

print()

numbers = [even , odd]
print(numbers)

print()
for number_list in numbers:
    print(number_list)
    for number in number_list:
        print(number)