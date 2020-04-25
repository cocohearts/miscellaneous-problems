import unittest
import P2

class TestP2(unittest.TestCase):
    def test1(self):
        self.assertEqual(P2.solve_problem([(7,1),(1,1),(15,1),(3,1),(10,0),(6,1)]),3)
    def test2(self):
        self.assertEqual(P2.my_sort([(7,1),(3,2),(5,4)]),[(3,2),(5,4),(7,1)])
    def test3(self):
        self.assertEqual(P2.my_sort([(19,1),(18,2),(17,3),(16,4)]),[(16,4),(17,3),(18,2),(19,1)])
    def test4(self):
        self.assertEqual(P2.my_sort([(7,1),(1,1),(15,1),(3,1),(10,0),(6,1)]),[(1,1),(3,1),(6,1),(7,1),(10,0),(15,1)])
if __name__ == "__main__":
    unittest.main()