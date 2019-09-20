list1=[i for i in range(1,50) if(i % 2)==0 ]
print(list1)

dict1={i:('yes'if i%4==0 or i%400==0 else'no') for i in range(2000,2050)}
print(dict1)

list2=[ i for i in range(1,100) for j in range(2,i)  if i != j and i % j == 0]
list3=[i for i in range(1,100) if i not in list2]
print(list3)

# printing the numbers divisible by 3 between 1 to 50

list4=[i for i in range(1,50) if i%3==0]
list5=['three' if i in list4 else i for i in range(1,50)]
print(list4)
print(list5)
