#!/bin/python3

import unittest
from codes.pos_finder import pos 


class TestPos(unittest.TestCase):
    
    def test_pos(self):
        text = "hello"
        p = pos(text)
        self.assertEqual(p["l"], [2, 3])
        self.assertEqual(p["h"], [0])
        
    
if __name__ == "__main__":
    unittest.main()