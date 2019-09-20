'''
3.Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
 If no odd number was entered, it should print a message to that effect.
'''
input_string=input("enter list of values seperated by space:\n")
list1=input_string.split()
print(list1)
max=0
for l in list1:
    if int(l)%2!=0 and int(l) > max:
        max=int(l)
print(max)

