import dependency_tree
import unittest
class DependencyTree(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(dependency_tree.solve_problem([(1,2),(1,3),(2,4),(3,4),(4,5)],[(1,3),(2,5),(3,4),(2,3),(4,2)]),[True,True,True,False,False])

    def test_case_2(self):
        self.assertEqual(dependency_tree.solve_problem([(1,2),(2,3),(3,1),(4,5),(5,6),(7,8)],[(1,3),(2,1),(3,5),(6,8),(7,8)]),[True,True,False,False,True])
    
    def test_case_3(self):
        self.assertEqual(dependency_tree.solve_problem([(1,2),(2,3),(3,4),(4,1),(1,7),(5,7),(6,5)],[(6,2),(6,7),(7,5),(3,1),(1,4)]),[False,True,False,True,True])

if __name__ == "__main__":
    unittest.main()