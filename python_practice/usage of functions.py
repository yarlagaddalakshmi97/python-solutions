'''
def sayhello():
    print("hello, welcome to the python world")
sayhello()
'''
#function with arguments
'''
def printint(a):
    print(a)
printint(1)
'''
# function with return statement
'''
def sum(a,b):
    c=a+b
    return c
z=sum(2,3)
print(z)
'''

#caller function vs called function
'''
def sum(a,b):
    c=a+b
    return c
def total():
    z=sum(7,3)
    if z==10:
        z=z+1
    print(z)
total()
'''
# returning two values from a function
'''
def ints(a,b):
  return a,b
temp1,temp2=ints(1,6)
print(temp1,temp2)
'''

def sum(a,b):
    c=a+b
    return a,b,c
temp1,temp2,temp3=sum(10,4)
print(temp1,temp2,temp3)

