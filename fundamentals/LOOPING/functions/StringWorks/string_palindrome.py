# create a function is_palindrome(word) retrun true if word is a palindrome
# else retrun false

word=input("Enter word")
def is_palindrome(word):
    reversed_str=word[::-1]
    return word==reversed_str
    print(is_palindrome(word))


