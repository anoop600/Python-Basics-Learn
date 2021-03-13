low = 1
high = 10000

print("Think of number between {} and {}".format(low, high))

input("Press Enter to start")

guess = 1
count = 1
while True:
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
