
import unittest
import collatz


class TestCollatz(unittest.TestCase):
    '''tests the collatz.py script'''

    def test_collatz(self):
        '''table driven test to verify collatz'''
        tests = ((742, 371),
                 (418, 209),
                 (118, 59),
                 (1978, 989))
        for test in tests:
            self.assertEqual(collatz.collatz(test[0]), test[1])

if __name__ == "__main__":
    unittest.main()

 