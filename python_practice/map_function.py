list1=list(input("enter a list:\n"))
print(list1)
print(list(map(lambda int1:int(int1)*2,list1)))

string4='11682390'
list4=list(map(lambda i:i+i,string4))
str3=''
for z in list4:
    str3=str3+z
print(int(str3))


input1='ACCENTURE'
list1=[]
for char in input1:
    list1.append(char)
print(list1)
list2=list(map(lambda z:z+'1',list1))
print(list2)
str=''
for char in list2:
    str=str+char
print(str)

