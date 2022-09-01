#!/bin/python3

import nltk
from nltk.corpus import stopwords


import sys

nltk.download('stopwords', download_dir="../data/nltk_data/")
nltk.data.path = ["../data/nltk_data/"]


def generate_N_grams(text, ngram=1):
    words = [word.strip() for word in text.split() if word not in set(stopwords.words('english')) and "-" not in word]
    # print(words)
    temp = zip(*[words[i:] for i in range(ngram)])
    ans = [' '.join(ngram) for ngram in temp]
    return ans


# print(generate_N_grams("North Carolina Department is very corruput 2-1-1", 3))
# print(generate_N_grams("service  Department pokemon", 3))
# def check_ngrams(l, ngram):
#     # print(l, ngram)
#     # print(l[0].split(" "))
#     return all([True if len(d.split(" ")) == ngram else False for d in l])


    

    