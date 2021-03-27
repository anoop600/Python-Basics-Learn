data = "Hi this is anoop"
print(data.split())

number = "1,23,456,7890,12345,678901"
output = number.split(sep=",")
print(output)

new_output = []
for index in range(len(output)):
    new_output.append(int(output[index]))

print(new_output)

new_output = []
for val in output:
    new_output.append(int(val))

print(new_output)