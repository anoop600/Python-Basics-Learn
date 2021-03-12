age = int(input("How old are you ? "))

all_good = "Have good day at work"
enjoy = "Enjoy the free time"
if age >=16 and age <=65:
    print(all_good)

if 16 <= age <= 65:
    print(all_good)

if age<16 or age >65:
    print(enjoy)
else:
    print(all_good)