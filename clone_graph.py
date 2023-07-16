from data_structures.graph import Node

class Solution:
    def __init__(self):
        self.visited: dict[int, Node] = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return 

        new_node = Node(node.val)
        self.visited[node.val] = new_node

        new_node.neighbors = [
            # (self.visited[child.val] if child.val in self.visited else self.cloneGraph(child)) for child in node.neighbors 
            (self.visited[child.val] if child.val in self.visited else self.cloneGraph(child)) for child in node.neighbors 
        ]

        return new_node
