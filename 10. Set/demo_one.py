#Syntax of set is similar to dictionary.
#If key-value pair is not specified then python creates dictionary
farm_animals = {"cow", "sheep", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print()
#Python has a class set using which we can create the SET
wild_animals = set(["lion", "tiger", "panther", "elephant"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)


print(farm_animals.intersection(wild_animals))
print(farm_animals.union(wild_animals))

even = set(range(0,40,2))
print(sorted(even))
squares_tuple = (4,6,9,16,15)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("square minus even")
print(squares.difference(even))
print(squares - even)

#difference_update update set on which it is called. return type is None
print("="*40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

#symmetric
even = set(range(0,40,2))
print(sorted(even))
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(sorted(squares))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))


#remove element from set
squares.discard(4)
squares.remove(16)
print(squares)
squares.discard(8) #if key not present it wont give error
#squares.remove(16) #Key error as key specified is not present
print(squares)

if 8 in squares: #manually handle key is present check
    squares.remove(8)

print(squares)

#Exception handling
try:
    squares.remove(8)
except KeyError:
    print("Item 8 is not member if squares set")