shoppinglist = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#Continue Statement
# for item in shoppinglist:
#     if (item != "spam"):
#         print("Buy {} ".format(item))

# print()

# for item in shoppinglist:
#     if (item == "spam"):
#         continue
#     print("Buy {} ".format(item))

#Break
find_item = "spam"
found_at = None
# for index in range(len(shoppinglist)):
#     if shoppinglist[index] == find_item:
#         found_at = index
#         break

if find_item in shoppinglist:
    found_at = shoppinglist.index(find_item)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("Item not found")