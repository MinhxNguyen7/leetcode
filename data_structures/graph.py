class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val: int = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []
        
