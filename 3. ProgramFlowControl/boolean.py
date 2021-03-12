day = "Saturday"
temp = 30
raining = False

if day == "Saturday" and temp > 27 and not raining:
    print("Go Swimming")
else:
    print("Learn Something")

print("-"*25)

if 0:
    print("True")
else:
    print("False")

name = input("Enter your name : ")

if name:
    print("Hi {} !".format(name))
else:
    print("Are you person with no name !! ")