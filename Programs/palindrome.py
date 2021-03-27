def palindrome(data):
    #return data == data[::-1]
    return data == "".join(reversed(data))

print(palindrome(input("Enter the string :")))