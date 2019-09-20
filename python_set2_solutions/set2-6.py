'''
6.Implement a function that satisfies the specification. Use a try-except block.

def findAnEven(l):
	"""Assumes l is a list of integers
	Returns the first even number in l
	Raises ValueError if l does not contain an even number"""
'''
'''
try:
    list1 = list(input("enter list of integers..:\n"))
    num = 0
    for l in list1:
        if int(l) % 2 == 0 and num == 0 and int(l)!=0:
            print(l)
            num = l
    if num == 0:
        raise ValueError
except ValueError:
    print("list does not contain an even number")
'''

list1=list(input("enter list\n"))
def findAnEven(l):
    for i in l:
        if int(i) % 2 == 0:
          return i
    else:
        raise ValueError
try:
     print(findAnEven(list1))
except ValueError:
    print("no even numbers in list")
