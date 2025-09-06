class Solution:
    @staticmethod
    def calculate_odd_even(n: int):
        """
        Returns the number of odd and even values in [1, n] in a tuple
        """
        div, mod = divmod(n, 2)
        
        odd = div + mod
        even = div

        return odd, even

    def flowerGame(self, n: int, m: int) -> int:
        # Same as how many odd-sum pairs (x, y) where 1 <= x <= n and 1 <= y <= m
        
        # Equal to even numbers <= n * odd numbers <= m
        # plus odd numbers <= n * even numbers <= m

        n_odd, n_even = Solution.calculate_odd_even(n)
        m_odd, m_even = Solution.calculate_odd_even(m)
        
        return n_even * m_odd + n_odd * m_even
