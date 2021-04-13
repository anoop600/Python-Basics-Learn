def is_palindrome(string: str) -> bool:
    """Function returns if the string passed is a palindrome

    Args:
        string ([str]): [string to check if its palindrome]

    Returns:
        [bool]: [return `True if palindrome` or `False`]
    """
    #return string.casefold() == string[::-1].casefold()
    return string.casefold() == "".join(reversed(string)).casefold()

def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


print(palindrome_sentence(input("Enter the string :")))