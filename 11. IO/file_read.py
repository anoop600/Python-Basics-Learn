#option 1
# jabber  = open("sample.txt", "r")
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end="")
# jabber.close()

#option 2
#using with is helpful as with with take care of closing the files once the operation is completed
# with open("sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end="")

#option 3
# with open("sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

#option 4
# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line, end='')

#option 5
# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')

#option 6
#This prints the string in reverse order
with open("sample.txt", "r") as jabber:
    lines = jabber.read()
print(lines)
for line in lines[::-1]:
    print(line, end='')