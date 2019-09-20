#global variable
x=10
def fun():
    global x
    x=x+12
    print(x)
fun()

#local variable
x=10
def fun():
    x=5
    x=x+12
    print(x)
fun()

#local vs global
x=10
def fun():
    global x
    x=5
    x=x+12
    print(x)
fun()


