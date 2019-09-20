list1=list(input("give  char values:\n"))
string1=''
for l in list1:
    string1=string1+l
print(string1)
string2=string1[::-1]
if string1==string2:
    print("palindrome")
else:
    print("not a palindrome")
