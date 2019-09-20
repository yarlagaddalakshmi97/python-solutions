'''
5.Implement a function that meets the specification below. Use a try-except block.
def sumDigits(s):
	"""Assumes s is a string
	Returns the sum of the decimal digits in s
	For example, if s is 'a2b3c' it returns 5"""
'''
s = input("enter a string mixed with intgers:\n")
def sumDigits(s):
    sum=0
    for char in s:
        if char.isnumeric():
            sum=sum+int(char)
    print(sum)
try:
    sumDigits(s)
except:
    print("error..try again")