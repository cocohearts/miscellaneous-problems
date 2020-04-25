import unittest
import P1

class TestP1(unittest.TestCase):
    def test1(self):
        self.assertEqual(P1.solve_problem("10001001000010"),2)
    def test2(self):
        self.assertEqual(P1.solve_problem("1001010001010100010100101"),2)
    def test3(self):
        self.assertEqual(P1.solve_problem("0000000100000100000010000100"),3)
    def test4(self):
        self.assertEqual(P1.solve_problem("0000000010000000"),7)
if __name__ == "__main__":
    unittest.main()