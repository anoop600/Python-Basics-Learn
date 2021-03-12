parrot = "Norwegian Blue"

letter = input("Enter the character : ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("Don't see that letter in word")