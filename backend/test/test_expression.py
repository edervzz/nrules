""" test """
import unittest

class TestExpression(unittest.TestCase):
    """_summary_"""
    def test_expression(self):
        """ Test- expression """
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


if __name__ == '__main__':
    print(__name__)
    unittest.main()
