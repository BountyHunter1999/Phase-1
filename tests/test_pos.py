#!/bin/python3

import unittest
from codes.pos_finder import pos 


class TestPos(unittest.TestCase):
    
    def test_pos(self):
        text = "je suis parle"
        self.assertEqual(pos(text), {i: d for i, d in enumerate(text)})
        
    
if __name__ == "__main__":
    unittest.main()