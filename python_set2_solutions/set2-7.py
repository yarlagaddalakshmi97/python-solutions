'''
7.A palindrome is a word that is spelled the same backward and forward, like "Malayalam" and "Noon" .
Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
 Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise.
 Remember that you can use the built-in function len to check the length of a string.
 Use the function definition

def isPalindrome(s):
	"""Assumes s is a str
	Returns True if s is a palindrome; False otherwise.
	Punctuation marks, blanks, and capitalization are
	ignored."""

'''
string1=input("enter a string:\n").upper().lower().replace(",",'').replace("'",'').replace('"','').replace(" ",'').replace("!",'')
def isPalindrome(string1):
    print(string1)
    if string1==string1[::-1]:
        print("palindrome ")
    else:
        print("not a palindrome")
isPalindrome(string1)
