#!/usr/bin/env python3.5
'''
Automate the Boring Stuff with Python
generic testing for chapter 4 projects
Jack Hayhurst
'''

from io import StringIO
import unittest
from unittest.mock import patch
import picture_grid


class TestPictureGrid(unittest.TestCase):
    '''tests the picture_grid.py script'''

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
            picture_grid.picture_grid(grid)
            self.assertEqual(fakeOutput.getvalue().strip(), output)

if __name__ == "__main__":
    unittest.main()
    