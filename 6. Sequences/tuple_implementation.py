t = ("a", "b", "c") 
print(t)

name = "anoop"
age = 25
print(name, age, "python", 2020)
print((name, age, "python", 2020))

#Accessing tuple
print(t)
print(t[0])
print(t[1])
print(t[2])

#Try updating tuple
#Tuple are immutable so data cannot be updated once created
# t[1] = "Anoop"
# print(t)

#Convert tuple to list
tuple2 = list(t)
print(tuple2)