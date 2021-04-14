list_one = {
    "a": "a",
    "b": "b",
    "c": "c",
}

print(list_one)

list_two = {
    "d": "d",
    "e": "e",
    "f": "f",
}

print(list_two)

print()

#Use of update will update the data in existing Dictionary
list_one.update(list_two)
print(list_one)

print()

list_two.update(list_one)
print(list_two)

#Use of copy will create new dictionary
nice_and_nasty = list_one.copy()
print(nice_and_nasty)