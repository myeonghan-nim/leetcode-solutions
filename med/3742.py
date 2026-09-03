class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # dp[j][c] = 현재 행의 j열까지 오면서 양수 칸을 c개 지났을 때의 최대 점수. 행을 한 줄씩 갱신하고, 마지막 칸에서 예산 이하의 최댓값을 고른다
        # 시간 복잡도: O(m·n·k)
        m, n = len(grid), len(grid[0])
        budget = min(k, m + n - 2)  # 경로 길이보다 큰 예산은 의미 없다
        NEG = -(10**15)

        dp = [[NEG] * (budget + 1) for _ in range(n)]
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                add_cost = 1 if v > 0 else 0
                cur = [NEG] * (budget + 1)

                if i == 0 and j == 0:
                    cur[0] = 0
                else:
                    for c in range(add_cost, budget + 1):
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
