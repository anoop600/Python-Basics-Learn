for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i,i**2,i**3))

print()

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i,i**2,i**3))

print()

for i in range(1,13):
    print("No. {0:2} squared is {1:>3} and cubed is {2:>4}".format(i,i**2,i**3))

print()

for i in range(1,13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i,i**2,i**3))

print()
print("PI = {0:12}".format(22/7))
print("PI = {0:<12f}".format(22/7))
print("PI = {0:<12.50f}".format(22/7))
print("PI = {0:<52.50f}".format(22/7))
print("PI = {0:<62.50f}".format(22/7))
print("PI = {0:<72.54f}".format(22/7))
age = 24
print(f"I am {age} old")

print(f"Pi = {22/7:12.50f}")

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[1:5])