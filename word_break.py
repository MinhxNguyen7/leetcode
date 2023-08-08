class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dictionary = set(wordDict)

        # After-the-end indices of starting substrings that are valid
        # I.e., valid_positions[i] = x means that s[:x] is a valid word sequence
        valid_positions: list[int] = [0]

        for idx in range(len(s)):
            for valid in valid_positions[::-1]:
                if s[valid:idx+1] in dictionary:
                    valid_positions.append(idx+1)
                    break

        return valid_positions[-1] == len(s)

if __name__ == '__main__':
    print(Solution().wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    ))