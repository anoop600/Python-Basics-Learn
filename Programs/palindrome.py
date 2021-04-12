def is_palindrome(string):
    #return string.casefold() == string[::-1].casefold()
    return string.casefold() == "".join(reversed(string)).casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


print(palindrome_sentence(input("Enter the string :")))