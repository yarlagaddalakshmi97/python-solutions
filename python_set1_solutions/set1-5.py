'''
5.Write a program that asks the user to enter an integer and prints two integers,
 root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
 If no such pair of integers exists, it should print a message to that effect.
'''
import math

from math import sqrt

number=int(input("enter an integer:\n"))
root=0
pwr=0
n=0
for i in range(1,number):
    root=i
    for j in range(1,6):
        pwr=j
        if root**pwr==number:
            n= root**pwr
            print("number:",number,"\nroot**pwr: ",root**pwr,"\nroot:",root,"\npwr:\n",pwr)
if n==0:
    print("no such pair exists..")


