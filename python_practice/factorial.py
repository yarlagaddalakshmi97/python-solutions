def fact(n):
    if n>0:
        return 1
    else:
        return n*fact(n-1)
res=fact(7)
print(res)