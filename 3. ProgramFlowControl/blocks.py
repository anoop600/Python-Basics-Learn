#IF Condition
# for i in range(1,13):
#     print("No. {} squared is {} cubed is {:4}".format(i, i**2,i**3))
# print("*"*80)

name = input ("Enter your name: ")
age = int(input("How old are you {0}? ".format(name)))
#print(age)

# if age >= 18:
#     print("Person can legally enough to vote")
#     print("Please put X in block")
# else:
#     print("Person is not legal enough to vote. Come back after {0} years".format(18-age))

if age < 18:
    if age < 0:
        print("You are not born !")
    print("Person is not legal enough to vote. Come back after {0} years".format(18-age))
elif age == 900:
    print("Sorry, you die in return of Jedi")
else:
    print("Person can legally enough to vote")
    print("Please put X in block")

