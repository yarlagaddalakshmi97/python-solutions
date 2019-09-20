input1=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
print(list(filter(lambda input1:input1>0,input1)))

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

input1=['a','b','c','d','e','f','g']
input2=['a','e',]
print(list(filter(lambda input3:input3 not in input2,input1)))

