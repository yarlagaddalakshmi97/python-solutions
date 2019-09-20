'''
i/'p:ask a string from user
o/p:count the character and print the string
i/p:accenture
o/p:a1c2e2n1t1u1r1
'''
'''
string1=input("enter a string :\n")
string2=""
for char in string1:
    string2=string2+char
    string2=string2+str(string1.count(char))
  # string2 =char+str(string1.count(char))
print(string2)
'''
'''
list1=list(input("enter a string :\n"))
dict1={}
for l in list1:
   dict1[l]=list1.count(l)
print(dict1)
'''
list1=list(input("enter a string :\n"))
dict1={}
for l in list1:
   dict1[l]=list1.count(l)
print(dict1)

string1=""
for key in dict1:
    string1=string1+key+str(dict1[key])
print(string1)

