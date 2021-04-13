fruits = {
    "orange": "orange_one",
    "apple": "apple_two",
    "lemon": "lemon_three",
}

print(fruits)
print(fruits['orange'])
print(fruits['apple'])
print(fruits['lemon'])

fruits["pear"] = "pear_four"
print(fruits)

print()

#delete particular key from dictionary
del fruits["pear"]
print(fruits)
print()

#del fruits
#print(fruits)

#Removes all items from the dictionary
# fruits.clear()
# print(fruits)

#If we try accessing they key which doesn't exist then gives error
# print(fruits['anoop'])

print(fruits)
while True:
    dict_key = input("Enter the fruit : ")
    if dict_key == "quit":
        break
    if dict_key in fruits:
        description = fruits.get(dict_key)
        print(description)
    else:
        print("We dont have the key '{}'".format(dict_key))
