inventory = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Mat", "HDMI Cable", "dvd-writer"]
current_choice = "-"

computer_parts = []
valid_choices = []

# valid_choices = [str(i) for i in range(1, len(inventory)+1)]
for i in range(1, len(inventory)+1):
    valid_choices.append(str(i))
print(valid_choices)
while current_choice != '0':
    # if current_choice in range(1, len(inventory)+1):
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        part = inventory[index]
        if part in computer_parts:
            #Its already exist
            print("Removing {}".format(current_choice))
            computer_parts.remove(part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(part)
        print("List now contains {}".format(computer_parts))
        # if current_choice == '1':
        #     computer_parts.append("Computer")
        # elif current_choice == '2':
        #     computer_parts.append("Monitor")
        # elif current_choice == '3':
        #     computer_parts.append("Keyboard")
        # elif current_choice == '4':
        #     computer_parts.append("Mouse")
        # elif current_choice == '5':
        #     computer_parts.append("Mouse Mat")
        # elif current_choice == '6':
        #     computer_parts.append("HDMI Cable")
    else:
        print("Please add options from the list below: ")
        # for i in range(0,len(inventory)):
        #     print("{}. {}".format(i+1,inventory[i]))
        for number,part in enumerate(inventory):
            #print("{}. {}".format(inventory.index(part)+1, part))
            print("{}. {}".format(number+1, part))
        # print("1. Computer")
        # print("2. Monitor")
        # print("3. Keyboard")
        # print("4. Mouse")
        # print("5. Mouse Mat")
        # print("6. HDMI Cable")
        print("0. to finish")
    current_choice = input()
else:
    print(computer_parts)