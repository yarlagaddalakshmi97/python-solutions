from sys import argv
if(len(argv)<3):
    print("insufficient arguments..can't proceed..please try again..")
elif argv[1]>argv[2] and argv[1]>argv[3]:
    print("argument 1 is largest..")
elif argv[1]>argv[2] and argv[1]<argv[3]:
    print("argument 3 is largest..")
elif argv[2]>argv[1] and argv[2]>argv[3]:
    print("argument 2 is largest..")
elif argv[2] > argv[1] and argv[3] > argv[2]:
    print("argument 3 is largest..")
else:
    print("the numbers are same..")