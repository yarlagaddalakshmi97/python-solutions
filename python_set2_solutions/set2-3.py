'''

3.Observe the following function definitions. They Calculate the Factorial as per the Mathematical definition 1! = 1 (n + 1)! = (n + 1) * n!
 Implement factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation

def factI(n):
	"""Assumes that n is an int > 0
	Returns n!
	Uses Iterative Implementation"""

def factR(n):
	"""Assumes that n is an int > 0
	Returns n!
	Uses Recursive Implementation"""

'''

# without using recursion
number = int(input("enter a number:\n"))
fact = 1
for i in range(1,number+1):
    fact = i * fact
print(fact)
# with recursion
number1 = int(input("enter a number:\n"))
def factorial(n):
    while(n>0):
        if n==1:
            return 1
        else:
            fact1=n*factorial(n-1)
            return fact1
print(factorial(number1))