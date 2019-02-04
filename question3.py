import random
import string
word = []
word2 = []
#creates a word and prints it
while len(word)<4:
    for i in range(65,122):
        asciinumbers = random.randrange(65,122)
        letter = chr(asciinumbers)
    word.append(letter)
print(word)
#creates a second word and prints it
while len(word2)<4:
    for i in range(65,122):
        asciinumbers = random.randrange(65,122)
        letter = chr(asciinumbers)
    word2.append(letter)
print(word2)
