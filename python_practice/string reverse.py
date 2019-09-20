string1=input("enter a string:\n")
string2=string1[::-1]
print(string1)
print(string2)
print(string1[0:6])
#without slicing
string1=input("enter a string:\n")
rev=''
for char in string1:
    rev=char+rev
print(rev)

