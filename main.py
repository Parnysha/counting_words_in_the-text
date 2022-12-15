import pandas as pd
import random
from matplotlib import pyplot as pl
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file',type=str)
args = parser.parse_args()
invitation = args.file
f = open(invitation)
all_words_with_simbols = f.read().split()
f.close()
all_words = []
for i in range(len(all_words_with_simbols)):
    row_with_letter = []
    for j in all_words_with_simbols[i]:
        if j.isalpha():
            if j.isupper():
                j = j.lower()
            row_with_letter.append(j)
        else:
            ''.join(j)
    all_words.append(''.join(row_with_letter))
dictionary = {}
for i in all_words:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1
sorted_dictionary = {}
sorted_keys = sorted(dictionary, key=dictionary.get)
sorted_keys.reverse()
k = 0
five_key = []
five_value = []
for i in sorted_keys:
    sorted_dictionary[i] = dictionary[i]
    if k < 5:
        five_key.append(i)
        five_value.append(sorted_dictionary[i])
        k += 1
pl.bar(five_key,five_value)
pl.show()
csv_data = pd.DataFrame({'Words':sorted_dictionary.keys(),'Total':sorted_dictionary.values()})
csv_data.to_csv(f'CSV_words{random.randint(0,1000000)}.csv', index=False,header=0)
print('CSV файл загружен')