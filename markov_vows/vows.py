import markovify

with open('vows.txt', 'r') as f:
    text = f.read()

vow_model = markovify.Text(text)

count = 0
for i in range(5):
    sentence = vow_model.make_short_sentence(100)
    limit = len(sentence.split(' '))
    count += limit
    print(limit, sentence)

print(count)
'''
Nicole,

You're the light in my life, my best friend, 

We've already been together half of our lives, my love for you is endless,
I can't wait to spend the rest of our lives together. I vow to always be by 
your side with every adventure,    


'''

import pandas as pd

df = pd.read_csv('songdata.csv')

queen = df[df['artist'] == 'Styx']

# for i in df.artist.unique():
#     print(i)
# print(queen.text)

print('*'*40)
queen_vow = markovify.Text(df.text)

for i in range(5):
    sentence = queen_vow.make_short_sentence(100)
    print(len(sentence.split(' ')), sentence)

