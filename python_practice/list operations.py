'''
str1 ="ACCENTURE"
list1 =[]
for char in str1:
    list1 =list1 +list( 2 *char)
print(list1)


list2 =[]
for char in str1:
    if char not in list2:
        list2 = list2 +list( 2 *char)

print(list2)


'''
'''
list1=[]
for char in str1:
    if char not in list:
        list1.append(char)
list1.extend(list1)
print(list1)'''
'''

print(list1.pop())
list1.insert(len(list1),'1')
print(list1)

li=[2,5,8]
def between():
    if li[0]>=li[1] and li[0]<li[1]:
        return 'true'
    else:
        return 'false'
print(between())
'''
#list with unique elements
li=[1,1,3,2,1,2,4,5,3]
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)