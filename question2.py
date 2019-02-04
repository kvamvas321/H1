import random
import string
word = []
while len(word)<4:
    for i in range(65,122):
        asciinumbers = random.randrange(65,122)
        letter = chr(asciinumbers)
    word.append(letter)
print(word)
