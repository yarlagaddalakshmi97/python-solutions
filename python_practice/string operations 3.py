'''
string='welcome'
str1=''
str2=''
count=-0
for char in string:
    if count<3:
        str1=str1+char
        count=count+1
    else:
        str2=str2+char
        count=count+1
print(str1)
print(str2)
'''
from math import sqrt

'''
print(eval('1+2'))

#  printing the even length strings
str3='this is a new batch in this year'
li=[]
for char in str3.split(' '):
    if len(char)%2==0:
        li.append(char)
print(li)

#first letter of each word in the string
str4='this is a new batch in this year'
l=str4.split(' ')
for char in l:
    print(char[0:1:1])
'''
#get the square root of integer if it is not an integer print wrong input
try:
    num1=int(input("enter a number:\n"))
    sqrt1=num1**(1/2)
    if type(sqrt1)=='int':
        print(sqrt1)
    else:
       raise ValueError
except ValueError:
    print('enter a valid number')
