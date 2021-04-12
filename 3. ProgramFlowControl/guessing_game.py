answer = 5

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

print("Please guess number between 1 and 10: ")

guess = get_integer(": ")

if guess != answer:
    if guess < answer:
        print("Guess Higher... Guess Again")
    else:
        print("Guess Lower... Guess Again")
    guess = get_integer(": ")
    if answer == guess:
        print("Guess Successful")
    else:
        print("Not Correctly guessed")
else:
    print("Got it in first Guess")
# if guess < answer:
#     print("Guess Higher... Guess again")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it")
#     else:
#         print("WRONGLY GUESSED")
# elif guess > answer:
#     print("Guess Lower... Guess again")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it")
#     else:
#         print("WRONGLY GUESSED")
# else:
#     print("Correctly Guessed")