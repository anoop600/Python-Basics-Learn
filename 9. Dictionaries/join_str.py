myList = ["a", "b", "c", "d"]

newString = ""

for char in myList:
    newString += char + ", "

print(newString)

#join method does not need a for loop outside for iteration. 
new_string_join = ", ".join(myList)
print(new_string_join)