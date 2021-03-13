low = 1
high = 1000

print("Think of number between {} and {}".format(low, high))

input("Press Enter to start")

guess = 1
count = 1
while low != high:
    guess = low + (high - low)//2
    print("low: {}, High: {}".format(low, high))
    high_low = input(
        "My guess is {}. Should I guess higher or lower? Enter h or l, or c is guess was correct : ".format(guess)).casefold()
    if high_low == 'h':
        # Guess Higher
        low = guess + 1
    elif high_low == 'l':
        # Guess Lower
        high = guess - 1
    elif high_low == 'c':
        print("Got it in {} guesses".format(count))
        break
    else:
        print("Enter h,l or c")
    count += 1
# Strange in Python we can use else for loops.
# If loop completes successfully then else block is executed.
# If in loop forcefully using break, then else block will not execute
else:
    print("You though of the number {} and you got in {}".format(low, count))
