class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        K = min(k, m + n - 2)
        NEG = -(10**15)

        dp = [[NEG] * (K + 1) for _ in range(n)]
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                add_cost = 1 if v > 0 else 0
                cur = [NEG] * (K + 1)

                if i == 0 and j == 0:
                    cur[0] = 0
                else:
                    for c in range(add_cost, K + 1):
                        best_prev = NEG
                        if i > 0:
                            best_prev = max(best_prev, dp[j][c - add_cost])
                        if j > 0:
                            best_prev = max(best_prev, dp[j - 1][c - add_cost])
                        if best_prev != NEG:
                            cur[c] = best_prev + v

                dp[j] = cur

        ans = max(dp[n - 1])
        return -1 if ans < 0 else ans
