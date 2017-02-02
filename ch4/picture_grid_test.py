#!/usr/bin/env python3.5
'''
Automate the Boring Stuff with Python
generic testing for chapter 4 projects
Jack Hayhurst
'''

from io import StringIO
import unittest
from unittest.mock import patch
import projects


class TestProjects(unittest.TestCase):
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
            self.assertEqual(projects.comma_code(testinput), testoutput)

    def test_picture_grid(self):
        '''single test to verify picture transfer'''

        grid = [['.', '.', '.', '.', '.', '.'],
                ['.', 'O', 'O', '.', '.', '.'],
                ['O', 'O', 'O', 'O', '.', '.'],
                ['O', 'O', 'O', 'O', 'O', '.'],
                ['.', 'O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O', '.'],
                ['O', 'O', 'O', 'O', '.', '.'],
                ['.', 'O', 'O', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.']]

        output = """
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
""".strip()

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            projects.picture_grid(grid)
            self.assertEqual(fakeOutput.getvalue().strip(), output)

if __name__ == "__main__":
    unittest.main()
    