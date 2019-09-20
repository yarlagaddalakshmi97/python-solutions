'''
i/'p:ask a string from user
o/p:count the character and print the dictionary
i/p:accenture
o/p:{a:1,c:2,e:2,n:1,t:1,u:1,r:1}
'''
'''
list1=list(input("enter a string :\n"))
dict1={}
for l in list1:
   dict1[l]=list1.count(l)
print(dict1)
'''
string1=(input("enter a string :\n"))
dict1={}
for char in string1:
   if char in dict1:
      dict1[char]=dict1[char]+1
   else:
      dict1[char]=1
print(dict1)


