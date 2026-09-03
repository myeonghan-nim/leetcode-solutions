class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # dp[i] = 인덱스 i에 도달하는 최대 점프 횟수. 앞선 모든 j에서 차이가 target 이내면 dp[j] + 1로 갱신한다
        # 시간 복잡도: O(n^2)
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]
