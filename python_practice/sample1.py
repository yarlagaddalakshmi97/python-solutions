list1=list(input("enter a string:\n").replace(' ','').upper().lower())
list2=[]
count=0
for i in list1:
	if ord(i)>=ord('a') and ord(i)<=ord('z'):
		if i not in list2:
			list2.append(i)
			count+=1
if count==26:
	print("entered sentence is a panagram")
else:
    print("sentence is not a panagram")
