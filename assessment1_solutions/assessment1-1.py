string1="""Hakka and Bukka were brothers and warriors. The brothers wanted to build their own kingdom where people could live without fear. They collected a band of young men and trained them in warfare. They lived in a forest hideout on the banks of the river Tungabhadra in South India.
One day, the brothers were out on a hunt. Ferocious dogs accompanied them. They crossed the river and rode on. A couple of frightened rabbits ran out of the bushes. The dogs gave them chase with the two brothers closely behind on their horses.
It was a long chase. The rabbits were running for their life. The dogs were catching up. Suddenly, in a swift move, the rabbits turned and faced the dogs. Taken aback by the show of defiance, the barking dogs stepped back. Hakka called back the dogs. As the dogs turned back, the rabbits walked away.
Hakka looked around. They were on the other side of the Tungabhadra. It was a rocky land. The sun was blazing in the sky.
"Strange! I've never seen rabbits challenging dogs before!" said Bukka.
"That’s the quality of this land," said a quiet voice, "Even rabbits give fight."
Startled to hear a stranger speak, the two brothers turned.
They saw a holy man walking towards them. He was a picture of peace. At the same time, his eyes were blazing bright."""
dict1={}
string1.replace('.','')
string1.replace('"','')
string1.replace("!",'')
string1.replace(",",'')
string1.replace("\n",' ')

for char in string1.split(" "):
    if char in dict1:
        dict1[char]=dict1[char]+1
    else:
        dict1[char]=1
print(dict1)
#length of string
print(len(string1))
#number of words
count=0
for v in dict1:
    count=count+dict1[v]
print(count)
#max occurrance
max=0
for w in dict1:
    if max<dict1[w]:
        max=dict1[w]
print(max)
#max ocurrance word
max=0
word=''
for w in dict1:
    if max<dict1[w]:
        max=dict1[w]
        word=w
print(word)
#repeated word's count
count1=0
for i in dict1:
    if dict1[i]>1:
        count1+=1
print(count1)
#repeated word's list
count1=0
list1=[]
for i in dict1:
    if dict1[i]>1:
        count1+=1
        list1.append(i)
print(list1)