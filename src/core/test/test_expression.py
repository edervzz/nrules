import unittest


class TestExpression(unittest.TestCase):

    def test_expression(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


if __name__ == '__main__':
    print(__name__)
    unittest.main()
