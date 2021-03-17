data = [104,105,110,120,130,4,130,150,160,350,170,5,183,185,187,188,191,360]

min_valid = 100
max_valid = 200

# for index in range(len(data)-1,-1,-1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data[index])
#         del data[index]
top_index = len(data)-1
for index,value in enumerate(reversed(data)):
    if value < min_valid or value >max_valid:
        print(top_index-index, value)
        del data[top_index-index]

print(data)

