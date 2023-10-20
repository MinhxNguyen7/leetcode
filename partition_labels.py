class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {char: index for index, char in enumerate(s)}

        ret = []
        until = 0
        length = 0
        for index, char in enumerate(s):
            length += 1
            until = max(until, last[char])
            if until == index:
                ret.append(length)
                length = 0

        return ret
    
if __name__ == '__main__':
    # Expect [9, 7, 8]
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))