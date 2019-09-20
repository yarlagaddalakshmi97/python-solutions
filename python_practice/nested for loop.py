'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")

for i in range(1,10):
    for j in range(1,i):
        print(j,end=" ")
    print("\n")

for i in range(1,10):
    for j in range(1,i):
        print("*",end=" ")
    print("\n")


for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print("\n")
'''

'''
n=int(input("enter a number:\n"))
for i in range(1,n+2):
    for j in range(1,i):
        print("*",end=" ")
    print("\n")

'''
'''
i=1
while(i<=5):
    print(i)
    i=i+1
'''

'''
i=1
while(i<=5):
    print(i)
    if(i==3):
        print("you have reached the limit....")
        print("bye")
        break
    i=i+1
'''

i=1
while(i<=5):
    print(i)
    i = i + 1
    if(i==3):
        print(i)
        continue

