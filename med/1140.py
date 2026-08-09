class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = piles[:]
        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]
        dp = [[0] * (n + 2) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix[i]
                else:
                    dp[i][m] = suffix[i] - min(dp[i + x][max(m, x)] for x in range(1, 2 * m + 1))
        return dp[0][1]
