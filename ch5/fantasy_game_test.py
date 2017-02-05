#!/usr/bin/env python3.5
'''
Automate the Boring Stuff with Python
Chapter 5 Projects
Tests the fantasy game script
'''
# by Jack Hayhurstfrom io import StringIO

from io import StringIO
import unittest
from unittest.mock import patch
import fantasy_game


class TestFantasyGame(unittest.TestCase):
    '''tests the fantasy_game.py script'''

    def test_displayInventory(self):
        '''
        tests displayInventory()
        '''

        test_input = {'rope': 1, 'torch': 6,
                      'gold coin': 42, 'dagger': 1, 'arrow': 12}

        expected_output = list('''
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
'''.strip().split()).sort()

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            fantasy_game.displayInventory(test_input)
            output_lines = fakeOutput.getvalue().strip().split('\n')
            self.assertEqual(output_lines[0], 'Inventory:')
            self.assertEqual(output_lines[-1], 'Total number of items: 62')

            lines = list(output_lines[1:-1]).sort()
            self.assertEqual(lines, expected_output)

    def test_addToInventory(self):
        '''
        tests addToInventory()
        '''

        test_data = (
            (
                {'gold coin': 42, 'rope': 1},
                ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'],
                {'gold coin': 45, 'rope': 1, 'dagger': 1, 'ruby': 1}
            ), (
                {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12},
                ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'],
                {'rope': 1, 'torch': 6, 'ruby': 1,
                 'gold coin': 45, 'dagger': 2, 'arrow': 12}
            )
        )

        for test in test_data:
            result = fantasy_game.addToInventory(test[0], test[1])

            self.assertEqual(test[2], result)


if __name__ == "__main__":
    unittest.main()
