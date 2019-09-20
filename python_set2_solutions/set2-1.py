'''
1.The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
 One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r).
 As a base case, we can use gcd(a, 0) = a.
 Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
num1=int(input("enter a number:\n"))
num2=int(input("enter another number:\n"))
print(gcd(num1,num2))