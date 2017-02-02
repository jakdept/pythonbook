#!/usr/bin/env python3.5
'''
Automate the Boring Stuff with Python
generic testing for chapter 4 projects

This test covers comma_code

Jack Hayhurst
'''

from io import StringIO
import unittest
from unittest.mock import patch
import comma_code


class TestCommaCode(unittest.TestCase):
    '''tests the collatz.py script'''

    def test_comma_code(self):
        '''table driven test to verify list combination'''
        tests = (('apples', 'bananas', 'tofu', 'cats',
                  'apples, bananas, tofu, and cats'),
                 ('apples', 'bananas', 5, 'cats',
                  'apples, bananas, 5, and cats'),
                 ('apples', 'bananas', 'tofu', True, 'cats',
                  'apples, bananas, tofu, True, and cats'))
        for testdata in tests:
            testinput, testoutput = (list(testdata[:-1]), str(testdata[-1]))
            self.assertEqual(comma_code.comma_code(testinput), testoutput)


if __name__ == "__main__":
    unittest.main()
    