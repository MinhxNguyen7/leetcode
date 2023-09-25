class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        count = 0

        starts = set(''.join(sorted(start_word)) for start_word in startWords)

        for target in targetWords:
            sorted_target = ''.join(sorted(target))
            
            count += any(
                (sorted_target[:omit] + sorted_target[omit+1:]) in starts 
                for omit in range(len(target))
            )

        return count