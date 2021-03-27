# This is concept of TUPLE
a = b = c = d = e = f = 12

print(a, b, c, d, e, f)

# RHS is a Tuple
x, y = 1, 2
print(x, y)

data = 1, 2, 3
print(data.__class__)  # Prints tuple
x, y, z = data
print(x, y, z)

# Unpacking the list
# We can unpack any sequence type
data_list = [12, 13, 14]
x, y, z = data_list
print(x, y, z)


# enumerate function returns the TUPLE
for i in enumerate("abcdefgh"):
    print(i, i.__class__)

index, character = (0, 'a')
print(index, character)

# enumerate function returns the TUPLE
for i in enumerate("abcdefgh"):
    index, character = i
    print(index, character)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1]*table[2])

name, length, width, height, price = table
print(length*width)

print()
albums = [("a", "b", 1),
          ("c", "d", 2), 
          ("e", "f", 3), 
          ("g", "h", 4)
          ]

for album in albums:
    name,track,year = album
    print(name, track, year)

print()
for name,track,year in albums:
    print(name, track, year)
