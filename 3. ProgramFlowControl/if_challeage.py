name = input("Enter name : ")
age = int(input("Enter age : "))

if 18 <= age < 31:
    print("Welcome to Club {} !".format(name))
else:
    print("Holiday is for cool people")