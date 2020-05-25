"""
Create a function that takes two parameters, paragraph and word, which
returns the sentence containing the word.
"""

p1 = 'Hello. How are you.'
w1 = 'you'

def word_list(paragraph, word):
    a = []
    for i in paragraph.split('.'):
        for j in i.split():
            if j == word:
                a.append(i)
    
    a = [x.strip() for x in a]

    return a



print(word_list(p1,w1))
