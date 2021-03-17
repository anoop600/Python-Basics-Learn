computer = ["cpu", "monitor", "memory", "hdd", "mouse", "keyboard"]

# for part in computer:
#     print(part)

# for i in range(len(computer)):
#     print(computer[i])

# print(computer[0:2])

# print(computer[-1])

print(computer)

# computer[3] = "trackball"
# print(computer)

print()

computer[3:4] = "trackball"
print(computer)

print()

data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]

# del data[:2]
# print(data)
# del data[13:]
# print(data)

min_valid = 100
max_valid = 200
stop = 0
# for index, value in enumerate(data):
#     if value < min_valid or value > max_valid:
#         del data[index]

# print(data)

for index, value in enumerate(data):
    if value >=min_valid:
        stop = index
        break
print(stop)
del data[:stop]

start = 0
for index in range(len(data)-1, -1, -1):
    if data[index] <= max_valid:
        start = index+1
        break

print(start)
del data[start:]
print(data)
