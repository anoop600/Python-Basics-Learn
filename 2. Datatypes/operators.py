a = 12
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)

print()

# This gives error as a/b gives floating point number but its expecting the integer
# for i in range(1,a/b):
#     print(i)

for i in range(1, a//b):
    print(i)

print(a+b/3-4*12)

print(a+(b/3)-(4*12))
