numbers = (1,2,3,4,5,6)

# print(numbers)
# print(*numbers)

def test_star(*args):
    print(args)
    for x in args:
        print(x)


# test_star(numbers)
test_star(0,1,2,3,4,5,6)

print()

test_star()