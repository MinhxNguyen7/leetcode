class Solution:
    VOWELS = {'a', 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def sortVowels(self, s: str) -> str:
        vowels = [c for c in s if c in Solution.VOWELS]
        vowels.sort()

        vowel_index = -1

        return "".join(
            c if c not in Solution.VOWELS else vowels[vowel_index := vowel_index + 1] 
            for c in s
        )

