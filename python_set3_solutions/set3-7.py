'''
7.Write a function named using_only() that takes a word and a string of letters,
 and that returns True if the word contains only letters in the list.
Can you make a sentence using only the letters acefhlo? Other than "Hoe alfalfa?"
'''
def using_only(word,letters):
    for char in word:
        if char not in letters:
            return 'word contain letters other than the given letters..'
        elif char==word[len(word)-1]:
            return 'true'
        else:
            continue
word = input("enter a word:\n")
letters = list(input("enter the letters`:\n"))
print(using_only(word, letters))


