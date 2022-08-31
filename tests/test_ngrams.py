#!/bin/python3

import sys
import unittest
from codes.n_grams import generate_N_grams

def check_ngrams(l, ngram):
    # print(l, ngram)
    # print(l[0].split(" "))
    return all([True if len(d.split(" ")) == ngram else False for d in l])



class TestNgrams(unittest.TestCase):
    
        
    def test_ngrams(self):
        text = "This is a nice way of doing things"
        d = generate_N_grams(text, 2)
        result = check_ngrams(d, 2)
        self.assertTrue(result, "This has to be True")

if __name__ == '__main__':
    
    # print(sys.argv)
    # fi = sys.argv[1]
    # n = int(sys.argv[2])


    
    # test_ngrams(d, n)
    # print("Test Passed!")
    unittest.main()