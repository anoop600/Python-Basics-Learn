import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

highest = 10
answer = random.randint(1,highest)
print(answer) # TODO: Remove this line after testing
print("Please guess number between 1 and 10: ")

guess = get_integer("Enter the number : ")

# if guess != answer:
#     if guess < answer:
#         print("Guess Higher... Guess Again")
#     else:
#         print("Guess Lower... Guess Again")
#     guess = int(input())
#     if answer == guess:
#         print("Guess Successful")
#     else:
#         print("Not Correctly guessed")
# else:
#     print("Got it in first Guess")
if guess == answer:
    print("Guess Success")
elif guess == 0:
    exit(0)
else:
    while answer != guess:
        print("Try again")
        guess = get_integer("Enter the number : ")
        if guess == answer:
            print("Guess Success")
            break
        if guess == 0:
            break