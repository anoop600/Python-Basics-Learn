available_exits = ["north", "south", "east","west"]

choosen_exit = ""

while choosen_exit not in available_exits:
    choosen_exit = input("Choose the direction : ")
    if  choosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("you got out of loop")