import os
import sys
import re


# def remove_punctuation(words):

#     finalwords = []
#     for word in words:
#         if (word.isalpha()) == True:
#             finalwords.append(word.lower())

#         elif (word.isalpha()) == False:
#             word = re.sub('[^A-Za-z]', '', word).lower()

#     return finalwords


# def make_sets(foo):
#     return set(formedwords)



# fileDir = os.path.dirname(os.path.realpath('__file__'))
# # print(fileDir)

# path = os.path.join(fileDir, 'books/republic.txt')
# wordlist = []

# with open(path, "r") as foo:
#     for x in foo:
#         wordlist.extend(x.split())

# formedwords = remove_punctuation(wordlist)

# # print(formedwords)
# print(make_sets(formedwords))

# settedwords = make_sets(formedwords)
# # print(len(formedwords))


filenames = ["alice_wonderland.txt", "don_quixote.txt", "frederick_douglass.txt",
             "iliad.txt", "peter_pan.txt", "pride_prejudice.txt", "republic.txt",
             "sherlock_holms.txt", "wizard_of_oz.txt"]
files = {}

# absFilePath = os.path.abspath(__file__)

fileDir = os.path.dirname(os.path.abspath(__file__))

# parentDir = os.path.dirname(fileDir)

path = os.path.join(fileDir, 'books')

for filename in filenames:
    with open(os.path.join(path, filename), "r", encoding="Latin-1") as file:
        if filename in files:
            continue
        files[filename] = file.read()

# for filename, text in files.items():
#     print(filename)
#     print("=" * 80)
#     print(text)

for x in files.keys():
    print(x)
