import unittest


class TestTest(unittest.TestCase):
    """
    Test class that will be torn down.
    """

    def test_pass(self):
        self.assertEqual(True, True)

    def test_fail(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
