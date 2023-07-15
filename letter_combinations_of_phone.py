from itertools import product

MAPPING = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution:
    @staticmethod
    def letterCombinations(digits: str):
        if len(digits) == 0:
            return
        
        yield from ("".join(x) for x in product(*(MAPPING[digit] for digit in digits)))