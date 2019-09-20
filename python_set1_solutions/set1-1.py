'''
1.Write a program that examines three variables—x, y, and z— and prints the largest odd number among them.
 If none of them are odd, it should print a message to that effect.
'''
a=int(input("enter a number:\n"))
b=int(input("enter another number:\n"))
c=int(input("enter third number:\n"))
if a%2==0:
    if b%2==0:
        if c%2==0:
            print("none of the given numbers is an odd number.....")
        else:
            print("largest odd number among the given numbers is:"+str(c))
    elif c%2!=0 and b>c:
        print(str(b)+" is the largest odd number among the given numbers ")
    else:
        print("largest odd number among the given numbers is:"+str(c))
elif b%2!=0 and c%2!=0 and a>b and a>c :
    print(str(a)+" is the largest odd number among the given numbers")
elif b%2!=0 and c%2!=0 and a>b and a<c:
    print("largest odd number among the given numbers is:" + str(c))
elif  b%2==0 and c%2!=0 and a<c:
    print("largest odd number among the given numbers is:" + str(c))
elif  b%2==0 and c%2!=0 and a>c:
    print("largest odd number among the given numbers is:" + str(a))
elif  b%2!=0 and c%2==0 and a>b:
    print("largest odd number among the given numbers is:" + str(a))
elif  b%2!=0 and c%2==0 and a<b:
    print("largest odd number among the given numbers is:" + str(b))
else:
    print("you have entered the same odd number thrice :"+str(a))
