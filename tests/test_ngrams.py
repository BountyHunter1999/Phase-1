#!/bin/python3

import sys
import unittest
# from codes.n_grams import generate_N_grams

def check_ngrams(l, ngram):
    # print(l, ngram)
    # print(l[0].split(" "))
    return all([True if len(d.split(" ")) == ngram else False for d in l])



class TestNgrams(unittest.TestCase):
    
    
    def test_file_1(self):
        """
        Checks for  1-grams
        """
        with open(f"data/ngram/1.txt", "r") as f:
            d = [data.strip() for data  in f.readlines()]
        result = check_ngrams(d, 1)
        self.assertTrue(result, "This has to be True")
    
    def test_file_2(self):
        """
        Checks for  2-grams
        """
        with open(f"data/ngram/2.txt", "r") as f:
            d = [data.strip() for data  in f.readlines()]
        result = check_ngrams(d, 2)
        self.assertTrue(result, "This has to be True")
    
    def test_file_3(self):
        """
        Checks for  3-grams
        """
        with open(f"data/ngram/3.txt", "r") as f:
            d = [data.strip() for data  in f.readlines()]
        result = check_ngrams(d, 3)
        self.assertTrue(result, "This has to be True")


if __name__ == '__main__':
    
    # print(sys.argv)
    # fi = sys.argv[1]
    # n = int(sys.argv[2])


    
    # test_ngrams(d, n)
    # print("Test Passed!")
    unittest.main()