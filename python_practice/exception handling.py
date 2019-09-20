a=int(input("enter a value :\n"))
b=int(input("enter another value :\n"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("please enter value other than zero for second value")
except:
    print("please try again....")
finally:
    print("well done...")
    c1=a+b
    print(c1)
