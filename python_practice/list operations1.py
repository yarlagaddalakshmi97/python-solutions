# getting an even numbers list and odd numbers list
'''list1=[]
list2=[]
for i in range(1,10):
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print(list1)
print(list2)'''

# count of digits and characters in a list

list2 = ['a', '1', 'b', '2', 'c', '3']

digit_count = 0
char_count = 0
for e in list2:
    if ord(e) >= ord('a') and ord(e) <= ord('z'):
        char_count = char_count + 1
    else:
        digit_count = digit_count + 1
print(digit_count)
print(char_count)

'''
list3=['a','1','b','2','c','3']
digit_count=0
char_count=0
for e in list3:
    if ord(e)>=65 and ord(e)<=122:
        char_count=char_count+1
    else:
        digit_count=digit_count+1
print(digit_count)
print(char_count)

'''






