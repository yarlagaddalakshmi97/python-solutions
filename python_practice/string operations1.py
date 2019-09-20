string='WELCOME'
#string is immutable
'''str[2]='l'
print(string)'''

#length of the string

count=0
for char in string:
    count=count+1
print(count)
#use len()
print(len(string))

#count of a particular character in a string

count1=0
for char in string:
    if char=='E':
        count1=count1+1
print(count1)
#use count()
print(string.count('E'))


