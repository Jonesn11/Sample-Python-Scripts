import unittest

import decompose_function


class TestCalc(unittest.TestCase):

    def test_decomposet(self):
        self.assertEqual(decompose_function.decomposet(11), [1, 2, 4, 10])


if __name__ == '__main__':
    unittest.main()
