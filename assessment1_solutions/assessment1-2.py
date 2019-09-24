'''
i/p:['five plus three', 'seven minus two', 'two plus eight minus five', 'eight divide four']
o/p:['eight', 'five', 'five', 'four']'''

list1=['five plus three', 'seven minus two', 'two plus eight minus five', 'eight divide four']
dict1={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'plus':'+','minus':'-','divide':'/'}
list2=[]
list3=[]
list4=[]
for i in list1:
    list2=i.split(' ')
    string1 =''
    for j in list2:
        string1=string1+str(dict1[j])
    list3.append(int(eval(string1)))
for i in list3:
    for k, v in dict1.items():
        if i==v:
            list4.append(k)
print(list4)

'''
ip_list = ['five plus three', 'seven minus two', 'two plus eight minus five', 'eight divide four']
ref_dict = {'plus': '+', 'minus': '-', 'divide': '/', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'seven': '7',
            'eight': '8'}
p_list = []
for i in ip_list:
    str_list = i.split(' ')
    string = ''
    for j in str_list:
        string = string + ref_dict[j]
    p_list.append(string)
op_list = []
for i in p_list:
     for j, k in ref_dict.items():
         if str(int(eval(i))) == k:
            op_list.append(j)
print(op_list)'''