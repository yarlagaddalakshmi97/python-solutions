'''
5.Write a function named avoids that takes a word and a string of forbidden letters,
 and that returns True if the word doesn’t use any of the forbidden letters.
'''

def avoids(word,forbidden):
    for char in word:
        if char in forbidden:
            return "the given word contains the forbidden letters.."
        elif char==word[len(word)-1]:
            return 'true'
word=input("enter a word:\n")
forbidden=list(input("enter the letters to forbid.:\n"))
print(avoids(word,forbidden))
