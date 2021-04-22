# with open("binary", "bw") as binary_file:
#     for i in range(17):
#         binary_file.write(bytes([i]))

with open("binary", "bw") as binary_file:
        binary_file.write(bytes(range(17)))


with open("binary", "br") as binary_file:
    for b in binary_file:
        print(b)