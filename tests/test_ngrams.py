#!/bin/python3
import sys


    
def test_ngrams(l, ngram):
    # print(l, ngram)
    # print(l[0].split(" "))
    for i in l:
        assert len(i.split()) == ngram, "Should be Equal"
    # return all([True if len(x.split()) == ngram else False for x in l])




if __name__ == '__main__':
    
    # print(sys.argv)
    fi = sys.argv[1]
    n = int(sys.argv[2])

    with open(f"data/ngram/{fi}.txt", "r") as f:
        d = [data.strip() for data  in f.readlines()]
    
    test_ngrams(d, n)
    print("Test Passed!")