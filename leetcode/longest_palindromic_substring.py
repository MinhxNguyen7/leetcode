class Solution:
    def longestPalindrome(self, s: str) -> str:
        def single_palindrome(idx: int) -> int:
            """
            Finds the longest palindrome centered at one letter
            """
            left = idx - 1
            right = idx + 1
            count = 1

            while left >= 0 and right < len(s):
                if s[left] != s[right]: break
                
                count += 2
                left -= 1
                right += 1
            
            return count

        def double_palindrome(idx: int) -> int:
            """
            Finds the longest palindrome centered on two letters
            """
            left = idx
            right = idx + 1
            count = 0

            while left >= 0 and right < len(s):
                if s[left] != s[right]: 
                    break
                count += 2
                left -= 1
                right += 1

            return count
        
        max_count = 1
        max_center = 0
        for i in range(len(s)):
            count = single_palindrome(i)
            if count > max_count:
                max_count = count
                max_center = i

        for i in range(len(s) - 1):
            count = double_palindrome(i)
            if count > max_count:
                max_count = count
                max_center = i
        
        if max_count % 2:
            return s[max_center - max_count // 2:max_center + max_count // 2 + 1]
        else:
            return s[max_center - max_count // 2 + 1:max_center + max_count // 2 + 1]

if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbd"))