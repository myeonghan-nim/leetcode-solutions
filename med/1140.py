class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i][m] = i번째 돌무더기부터 시작하고 M = m일 때 현재 차례 플레이어가 가져갈 수 있는 최대 돌 수. 남은 전체 합(suffix)에서 상대가 최선으로 가져갈 값을 뺀다
        # 시간 복잡도: O(n^3)
        n = len(piles)
        suffix = piles[:]
        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]
        dp = [[0] * (n + 2) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:  # 남은 돌을 한 번에 모두 가져갈 수 있다
                    dp[i][m] = suffix[i]
                else:
                    dp[i][m] = suffix[i] - min(dp[i + x][max(m, x)] for x in range(1, 2 * m + 1))
        return dp[0][1]
