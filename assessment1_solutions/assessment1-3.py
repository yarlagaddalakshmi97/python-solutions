'''
Check the given number is palindrome or not??
'''
number=int(input("enter a number..\n"))
temp=number
reverse=0
while(temp>0):
    remainder=temp%10
    reverse=reverse*10+remainder
    temp=temp//10
if number==reverse:
    print("given number is a palindrome..")
else:
    print("not a palindrome")