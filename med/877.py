class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + length - 1] - dp[i])
        return dp[0] > 0
