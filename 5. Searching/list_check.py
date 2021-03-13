numbers = [1,25,32,12,60]

for num in numbers:
    if num % 8 ==0:
        print("Number is not accepted")
        break
else:
    print("All number looks good")