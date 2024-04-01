from tester import test

class Mapping:
    def __init__(self):
        self._dict: dict[str, int] = {}
        self.next_index = 0

    def get(self, char: str):
        if char not in self._dict:
            self._dict[char] = self.next_index
            self.next_index += 1
        return self._dict[char]

class Solution:
    @staticmethod
    def hashFunc(word: str) -> tuple[int, ...]:
        mapping = Mapping()

        return tuple(
            mapping.get(char) for char in word
        )

    @staticmethod
    def findAndReplacePattern(words: list[str], pattern: str) -> list[str]:
        pattern_hash = Solution.hashFunc(pattern)
        ret = []

        for word in words:
            if Solution.hashFunc(word) == pattern_hash:
                ret.append(word)

        return ret

if __name__ == '__main__':
    test(
        ["mee","aqq"],
        Solution.findAndReplacePattern,
        words = ["abc","deq","mee","aqq","dkd","ccc"],
        pattern = "abb"
    )
    
    test(
        ["a","b","c"],
        Solution.findAndReplacePattern,
        words = ["a","b","c"],
        pattern = "a"
    )
