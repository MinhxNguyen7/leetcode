from functools import lru_cache

# https://leetcode.com/problems/palindrome-partitioning/solutions/1667786/python-simple-recursion-detailed-explanation-easy-to-understand/
class Solution:
    @staticmethod
    @lru_cache
    def partition(s: str):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in Solution.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
                    
    
if __name__ == '__main__':
    # print(Solution().partition("aaaa"))
    # print(Solution().partition("efe"))
    print(list(Solution().partition("abbab")))