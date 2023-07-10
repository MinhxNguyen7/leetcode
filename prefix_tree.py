class Node:
    def __init__(self):
        self.children: dict[str, 'Node|None'] = {}
    
    def __getitem__(self, char: str):
        return self.children[char]

    def __setitem__(self, char: str, item: 'Node|None'):
        self.children[char] = item

    def __contains__(self, char: str):
        return char in self.children
    


class Trie:

    def __init__(self):
        self.head: Node = Node()

    def insert(self, word: str) -> None:
        node: Node = self.head

        for char in word:
            if not char in node:
                node[char] = Node()
            node = node[char]

        node[""] = None # Sentinel to mark that a word ends here

    def search(self, word: str) -> bool:
        node = self.head

        for char in word:
            if not char in node: return False
            node = node[char]
        
        return "" in node

    def startsWith(self, prefix: str) -> bool:
        node: Node = self.head

        for char in prefix:
            if not char in node: return False
            node = node[char]
        
        return True
    
if __name__ == '__main__':
    tree = Trie()
    
    tree.insert("apple")
    print(tree.search("apple"))
    print(tree.startsWith("app"))