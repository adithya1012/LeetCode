import unittest

def sum_of_2(a,b):
    return a+b

class TestCases(unittest.TestCase):
    def test_simpleadd(self):
        self.assertEqual(sum_of_2(1,2), 3)

    def test_wrong(self):
        self.assertEquals(sum_of_2(2, 2), 4)


# obj = TestCases()

