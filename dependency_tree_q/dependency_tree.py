"""
Input: a list of tuples [(1,2),(2,3),(1,3),(3,4),(2,4)] makes a graph like this 
"""
class Node:
    def __init__(self,key):
        self.key = key
        self.children = set([])


    @staticmethod
    def insert(key1,key2):
        if not key1 in Node.list_nodes:
            node1 = Node(key1)
            Node.list_nodes[key1] = node1
        else:
            node1 = Node.list_nodes[key1]

        if not key2 in Node.list_nodes:
            node2 = Node(key2)
            Node.list_nodes[key2] = node2
        else:
            node2 = Node.list_nodes[key2]

        node1.children.add(node2)

    def descendants(self,our_set,visited_nodes):
        if self.children:
            our_set.update(self.children)
            if not self in visited_nodes:
                visited_nodes.add(self)
                for child in self.children:
                    child.descendants(our_set,visited_nodes)
        else:
            return

    def dependent(self,key):
        node = self.list_nodes[key]
        our_set = set([self])
        visited = set([])
        self.descendants(our_set,visited)
        return (node in our_set)

def solve_problem(list_tuples,list_questions):
    # setup:
    Node.list_nodes = {}
    for my_tuple in list_tuples:
        Node.insert(my_tuple[0],my_tuple[1])
    output_list = []
    for question in list_questions:
        output_list.append(Node.dependent(Node.list_nodes[question[0]],question[1]))
    return output_list