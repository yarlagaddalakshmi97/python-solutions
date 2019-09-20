'''
4.Write a program that computes the decimal equivalent of the binary number 10011?
'''
string1='10011'
count=len(string1)-1
number=0
for char in string1:
    number=number+(int(char)*(2**count))
    count-=1
print(number)



