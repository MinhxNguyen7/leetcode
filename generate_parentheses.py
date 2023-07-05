from itertools import chain
from typing import Iterable

class Solution:
    @staticmethod
    def recurse(original: str, opens: int, limit: int) -> Iterable[str]:
        chars_remaining = limit - len(original)
        
        if opens > chars_remaining:
            return tuple()
        
        if opens == chars_remaining:
            return (original + ")"*chars_remaining,)
        
        if opens == 0:
            return Solution.recurse(original + "(", 1, limit)
        
        if opens == chars_remaining == 1:
            return (original + ")",)

        # Can either open or close
        return chain(
            Solution.recurse(original + "(", opens + 1, limit), 
            Solution.recurse(original + ")", opens - 1, limit)
        )
        
    def generateParenthesis(self, n: int) -> Iterable[str]:
        return Solution.recurse("", 0, n * 2)
    
    
print([x for x in Solution().generateParenthesis(3)])