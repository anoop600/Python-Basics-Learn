answer = 5

print("Please guess number between 1 and 10: ")

guess = int(input())

if guess != answer:
    if guess < answer:
        print("Guess Higher... Guess Again")
    else:
        print("Guess Lower... Guess Again")
    guess = int(input())
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