#!/usr/bin/env python3.5
'''
Tests the printTable() function
'''


from io import StringIO
import unittest
from unittest.mock import patch
import printTable


class TestPrintTable(unittest.TestCase):
    '''tests the printTable.py script'''

    def test_printTable(self):
        '''
        tests printTable()
        '''

        test_data = (
            ([['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']],
             '''
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
            '''),
            ((('DarkBlue', 'Green', 'Purple', 'Mauv', 'Orange', 'Crimson', 'Blue',
               'Fuscia', 'Mauv', 'Blue'),
              ('Yaozhou', 'Debar', 'Corupá', 'Ami', 'Vrbno pod Pradědem', 'Buenavista',
               'Aveiras de Cima', 'Hutang', 'Puerto Berrío', 'Waterbury'),
              ('Yakijo', 'Roodel', 'Devpulse', 'Kamba', 'Pixonyx',
               'Jabbersphere', 'Voonte', 'Zazio', 'Jazzy', 'Thoughtbridge'),
              ('utilisation', 'workforce', 'asynchronous', 'conglomeration',
               'hub', 'regional', 'Future-proofed', 'collaboration',
               'Adaptive', 'attitude-oriented')),
             '''
DarkBlue            Yaozhou        Yakijo       utilisation
   Green              Debar        Roodel         workforce
  Purple             Corupá      Devpulse      asynchronous
    Mauv                Ami         Kamba    conglomeration
  Orange Vrbno pod Pradědem       Pixonyx               hub
 Crimson         Buenavista  Jabbersphere          regional
    Blue    Aveiras de Cima        Voonte    Future-proofed
  Fuscia             Hutang         Zazio     collaboration
    Mauv      Puerto Berrío         Jazzy          Adaptive
    Blue          Waterbury Thoughtbridge attitude-oriented
'''))

        for test in test_data:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                printTable.printTable(test[0])
                output_lines = fake_output.getvalue().strip().split('\n')
                expected_lines = test[1].strip().split('\n')
                self.assertEqual(output_lines , expected_lines)

if __name__ == "__main__":
    unittest.main()
