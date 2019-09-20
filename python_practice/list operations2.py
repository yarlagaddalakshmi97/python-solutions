#list to dictionary
'''
i/p:['one',1,'two',2,'three',3,'four',4,'five',5,'five',5]
o/p:{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': [5, 5]}
'''

list1=['one',1,'two',2,'three',3,'four',4,'five',5,'five',5]
dict={}
for i in range(0,len(list1),2):
    if list1[i] in dict:
        li = [dict[list1[i]], list1[i+1]]
        dict[list1[i]] = li
    else:
        dict[list1[i]]=list1[i+1]
print(dict)


