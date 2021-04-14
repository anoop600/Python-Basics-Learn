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
print(sorted(e))