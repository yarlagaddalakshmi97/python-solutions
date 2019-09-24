'''
2.Write a function called rotate_word() that takes a string and an integer as parameters,
and that returns a new string that contains the letters from the original string "rotated" by the given amount. For example,
 "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed". You might want to use the built-in functions ord,
which converts a character to a numeric code, and chr, which converts numeric codes to characters.
'''

def rotate_word(str,num):
    string=''
    for char in str:
        string=string+chr(ord(char)+num)
    print(string)
string1=input("enter a string:\n")
int1=int(input("enter a number:\n"))
rotate_word(string1,int1)
