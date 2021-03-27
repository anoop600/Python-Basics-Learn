alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]

for alphabet in alphabets:
    print(alphabet)

separator = " | "
output = separator.join(alphabets)
print(output)

print(", ".join(alphabets))