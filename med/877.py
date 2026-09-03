class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i] = 구간 [i, i+length-1]에서 선공이 후공보다 더 가져가는 돌의 차이. 1차원 배열을 길이 순으로 갱신해 공간을 줄인다
        # 시간 복잡도: O(n^2)
        n = len(piles)
        dp = piles[:]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + length - 1] - dp[i])
        return dp[0] > 0
