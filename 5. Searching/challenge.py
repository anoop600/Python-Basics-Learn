def option():
    print("""
    Please choose your option from the list below : 
    1. \tLearn Python
    2. \tLearn Java
    3. \tGo Swimming
    4. \tHave dinner
    5. \tGo to bed
    0. \tExit
    """)

option()
choice = '-'
while choice != 0:
    choice = int(input())
    if choice in range(1, 7):
        print("You chose {}".format(choice))
    else:
        option()

# while True:
#     choice = int(input())
#     if choice == 0:
#         break
#     elif choice in range(1, 7):
#         print("You chose {}".format(choice))
#     else:
#         option()
