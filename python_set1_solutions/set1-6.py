'''
6.Let s be a string that contains a sequence of decimal numbers separated by commas,
 e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.
'''
string=input("enter the string of numbers seperated by comma :\n")
list1=string.split(',')
sum=0
for l in (list1):
    sum=sum+float(l)
print(sum)