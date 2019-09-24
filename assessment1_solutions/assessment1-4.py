'''
find prime numbers for given range .. input : 2 numbers find the range and display list of prime numbers
'''
start_value=int(input("enter the start value:\n"))
end_value=int(input("enter the end value:\n"))
list1=[]
for i in range(start_value,end_value+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        list1.append(i)
print(list1)