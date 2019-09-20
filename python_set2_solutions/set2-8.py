'''
8.The built-in function eval takes a string and evaluates it using the Python interpreter. For example:

eval('1 + 2 * 3')
7
import math
eval('math.sqrt(5)')
2.2360679774997898
 eval('type(math.pi)')
<type 'float'>

Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval,
 and prints the result. It should continue until the user enters 'done', and then return the value of the last expression it evaluated.

'''

def eval_loop():
    value = ''
    while(1==1):
        string1=input("enter a string:\n").upper().lower()
        if string1!='done':
          value=eval(string1)
          print(value)
        else:
            print(value)
            return
eval_loop()


