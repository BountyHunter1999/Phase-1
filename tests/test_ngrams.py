#!/bin/python3
import sys

# print(sys.argv)
fi = sys.argv[1]
n = int(sys.argv[2])

with open(f"data/ngram/{fi}.txt", "r") as f:
    d = [data.strip() for data  in f.readlines()]
    
def check_ngrams(l, ngram):
    # print(l, ngram)
    # print(l[0].split(" "))
    return all([True if len(x.split()) == ngram else False for x in l])


if check_ngrams(d, n):
    print(f"{fi}.txt contents are {n}-gram")
else:
    print(f"{fi}.txt contents aren't {n}-gram")

