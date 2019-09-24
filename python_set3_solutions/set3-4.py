'''
4.Modify the above program to print only the words that have no “e” and compute the percentage of the words in the list have no “e.”
'''
def has_no_e(words):
    list2=[]
    for i in words:
        char=i
        for j in range(0,len(i)):
            if char[j]=='e'or char[j]=='E':
                break
            elif j==len(char)-1:
                list2.append(i)
    print(list2)
    print("percentage of words  that have no 'e':",(len(list2)/len(words))*100)
words=input("enter a list of words:\n").split()
print(has_no_e(words))