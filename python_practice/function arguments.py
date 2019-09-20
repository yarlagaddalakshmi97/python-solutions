# required arguments--mandatory to give the arguments during function calling
def fun(name):
    print(name)


# fun()
fun('laxmi')


# keyword arguments---we can give the arguments in any order
def fun1(name, age):
    print(name)
    print(age)


fun1(age=10, name="princess")


# default arguments---given while defining the function
def fun2(name, age=15):
    print(name)
    print(age)


fun2(name="prince")


# variable length arguments
def fun3(function, *args):
    sum = 0
    if function == 'add':
        for i in args:
            sum = sum + i
    print(sum)


fun3('add', 2, 23, 4)
fun3('add', 1, 2, 2, 2, 3)


# variable length keyword args
def fun4(name, **kwargs):
    print(name)
    for i in kwargs:
        print(i)

fun4("princess",class1=5,rank=10,age=10)
