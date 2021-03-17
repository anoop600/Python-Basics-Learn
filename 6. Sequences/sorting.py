pengram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pengram)

print(letters)

numbers_list = [2.4, 5.1, 1.1, 9.8, 5, 4, 3.3]
print("ID of numbers_list = {}".format(id(numbers_list)))

print()

numbers = sorted(numbers_list)
print(numbers)
print("ID of numbers_list = {}".format(id(numbers)))

print()

numbers_list.sort()
print(numbers_list)
print("ID of numbers_list = {}".format(id(numbers_list)))

# sort -> Updates the same list -> No return statement
# sorted -> Created/Returns new list with the data

missing_letter = sorted(
    "The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

print()

name = ["Graham", "Anoop", "Terry", "Jerry", "eric", "terry", "anoop"]

name.sort(key=str.casefold)
print(name)