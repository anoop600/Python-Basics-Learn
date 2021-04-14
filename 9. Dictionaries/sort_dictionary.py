fruits = {
    "orange": "orange_one",
    "apple": "apple_two",
    "lemon": "lemon_three",
}

print(fruits)

print()
ordered_keys = list(fruits.keys())
print(ordered_keys)

print()
ordered_keys.sort()
print(ordered_keys)

# new_list_key = sorted(ordered_keys)
# print(new_list_key)

for f in ordered_keys:
    print(f)

print()
for f in sorted(fruits.keys()):
    print(f)

print(fruits.keys())
print(fruits.values())

print(fruits.items())
f_tuple = tuple(fruits.items())
print(f_tuple)