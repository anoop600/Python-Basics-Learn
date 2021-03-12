#         01234567890123
parrot = "Norwegian Blue"

print(parrot)

# # print(parrot[3])

# #POSITIVE INDEX
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# #Negative Index
# print()
# print("Using Negative index")
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# #Subtract String Length
# print()
# print(len(parrot))
# parrot_string_length = len(parrot)
# print(parrot[3-parrot_string_length])
# print(parrot[4-parrot_string_length])
# print(parrot[9-parrot_string_length])
# print(parrot[3-parrot_string_length])
# print(parrot[6-parrot_string_length])
# print(parrot[8-parrot_string_length])

# Slice
# Second value in index is excluded
# print(parrot[0:5])
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])

# print(parrot[-4:])
# print(parrot[10:14])
# print(parrot[10:])
# print(parrot[:6]+parrot[6:])
# print(parrot[:])

# # NEgative index in slices
# print(parrot[-4:12])
# print(parrot[-4:-2])

#Strip String

#         01234567890123
# parrot = "Norwegian Blue"

# print(parrot[0:6:2]) #selects character in index 0,2,4,...
# print(parrot[0:6:3]) #selects character in index 0,3,6,...

# number = "9,223;372:036 854,775;807"
# print(number[2::4])  #230878
# print(number[1::4])

# seperators = number[1::4]
# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])

#Slice Backword

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

#reverse the string
backwards = letters[::-1]
print(backwards)

#qpo
print(letters[16:13:-1])
#edcba
print(letters[4::-1])
#last 8 character in rev order
print(letters[:-9:-1])

print(letters[-4:])

print(letters[-1:])
print(letters[:1])