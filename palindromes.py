import os
import random

# random.seed(a=None, version=2)
# print(random.getstate()) 

# Load file and put it to dictionary as set
dictionary = {word.rstrip(os.linesep) for word in open('word-list-7-letters.txt')}
 
# List of results
results = []
for word in dictionary:
    # [::-1] reverses string
    reversed_word = word[::-1]
    if reversed_word in dictionary and word > reversed_word:
        results.append((word, reversed_word))
 
print(len(results))
for words in random.sample(results, len(results)):
    print(' '.join(words))