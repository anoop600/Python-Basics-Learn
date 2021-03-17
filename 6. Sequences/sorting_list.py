even = [2,4,6,8]
odd = [1,3,5,7,9]

even.extend(odd)
print(even)

#Sort method will not create new list insted it uses the same list
even.sort()
print(even)
print(id(even))


even.sort(reverse=True)
print(even)
print(id(even))
# even.reverse()
# print(even)