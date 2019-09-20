'''
7.Write a function isIn() that accepts two strings as arguments and returns True if either string occurs anywhere in the other,
 and False otherwise. Hint: you might want to use the built-in str operation in.
'''
string1=input("enter a string :\n")
string2=input("enter another string :\n")
def isIn(string1,string2):
    if string2 in string1:
        print("given second string is a substring of the first string...")
    else:
        print("given second string is not a substring of the first string...")
isIn(string1,string2)
