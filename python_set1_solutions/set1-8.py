'''

8.Implement a function that satisfies the specification. Use a try-except block.

def getRatios(vect1, vect2):
	"""Assumes: vect1 and vect2 are lists of equal length of numbers
	Returns: a list containing the meaningful values of
	vect1[i]/vect2[i]"""

'''
str1=input("enter list of values seperated with comma:\n")
str2=input("enter another list of values seperated with comma:\n")
list1=str1.split(',')
list2=str2.split(',')
list3=[]

try:
    for i in range(0,len(list1)):
        z=int(list1[i])//int(list2[i])
        print(z)
        list3.append(z)
except ZeroDivisionError:
    print("please give the values  greater than zero..")
'''except :
    print("enter the same length of elements for both the lists..")'''
print(list1)
print(list2)
print(list3)