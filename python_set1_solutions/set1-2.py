'''
2.Python provides a built-in function called len that returns the length of a string, so the value of len('Cigna') is 5.
 Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces
  so that the last letter of the string is in column 70 of the display.

 right_justify('Cigna')
'''
from operator import index

s=input("enter a string:\n")
z=" "
spaces=70-len(s)
def rigt_justify(s):
    for char in s:
        if s.find(char)==0:
            print(z*spaces,s)
rigt_justify(s)
