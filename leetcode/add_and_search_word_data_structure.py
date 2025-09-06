class Node:
    def __init__(self):
        self.children: dict[str, 'Node'] = {}
    
    def __getitem__(self, char: str):
        return self.children[char]

    def __setitem__(self, char: str, item: 'Node'):
        self.children[char] = item

    def __contains__(self, char: str):
        return char in self.children
    
    def search(self, string: str) -> bool:
        """
        Recursively searches from this node whether there's a match
        """
        if string == "" and "" in self: return True
        
        node = self
    
        for idx, char in enumerate(string):
            if char == ".":
                sub_search = string[idx + 1:]
                # return any(child.search(sub_search) for key, child in self.children.values() if key != "")
                for key, child in node.children.items():
                    if key == "": continue
                    
                    if child.search(sub_search) == True: return True
                return False
                    
            if not char in node: return False
            node = node[char]
        
        return "" in node


class WordDictionary:

    def __init__(self):
        self.head: Node = Node()

    def addWord(self, word: str) -> None:
        node: Node = self.head

        for char in word:
            if not char in node:
                node[char] = Node()
            node = node[char]

        node[""] = Node() # Sentinel to mark that a word ends here

    def search(self, word: str) -> bool:
        return self.head.search(word)
    
if __name__ == '__main__':
    d = WordDictionary()
    
    for word in ["at","and","an","add", "bat"]:
        d.addWord(word)

    print(d.search("b."))
    
    
    