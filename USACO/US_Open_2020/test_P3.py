import unittest
import P3

class TestP3(unittest.TestCase):
    def test1(self):
        self.assertEqual(P3.bash_check(2,1,4,[[2,3],[2,4],[1,2]]),"1100")
    def test2(self):
        self.assertEqual(P3.solve_problem(4,[(7,1,2),(5,2,3),(6,2,4)],"1100"),"1 1 Infinity")
    def test3(self):
        self.assertEqual(P3.solve_problem(4,[(7,1,2),(5,2,3),(6,2,4)],"0010"),"1 0 0")
    def test4(self):
        self.assertEqual(P3.solve_problem(4,[(7,1,2),(5,2,3),(6,2,4)],"1111"),"2 2 Infinity")
    def test5(self):
        self.assertEqual(P3.solve_problem(4,[(7,1,2),(5,2,3),(6,2,4)],"0111"),"2 1 2")
    def test6(self):
        self.assertEqual(P3.solve_problem(4,[(7,1,2),(5,2,3),(6,2,4)],"0110"),"1 1 1")
if __name__ == "__main__":
    unittest.main()