int1=int(input("enter an integer to check whether it is palindrome or not..:\n"))
temp=int1
rev=0
while (int1>0):
    rem=int1%10
    rev=rev*10+rem
    int1=int1//10
print(rev)
if (temp==rev):
    print("yes palindrome..")
else:
    print("not a palindrome..")