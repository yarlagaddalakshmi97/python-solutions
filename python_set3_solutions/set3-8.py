'''
8.Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok).
 How many abecedarian words are there? (i.e) "Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"
'''
def abecedarian(words):
    for i in words:
        for j in (0,len(i)):
            if ord(i[j])>ord[j+1]:
                print(i[j])
                break
            elif i[j]==i[len[i]-1]:
                return i
            else:
                continue

words = input("enter words:\n").split(" ")
print(words)
print(abecedarian(words))



