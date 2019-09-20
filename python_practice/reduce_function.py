

from functools import reduce
list2=[1,2,3,4]
print(list[1])
mul=1
for i in list2:
    mul=mul*int(i)
print(mul)

print(reduce(lambda arg1,arg2:arg1*arg2,list2))
