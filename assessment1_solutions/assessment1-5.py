'''
find anagram for two given string ex. add, dad --> anagram
'''
'''
string1=input("enter a string:\n")
string2=input("enter another string:\n")
count=0
for char in string1:
    if char in string2:
        count+=1
if count==len(string1):
    print("anagram")
else:
    print("not an anagram")
'''
string1=input("enter a string:\n")
string2=input("enter another string:\n")
list1=sorted(string1)
list2=sorted(string2)
if list1==list2:
    print("anagram\n")
else:
    print("not an anagram\n")
print(list1)
print(list2)