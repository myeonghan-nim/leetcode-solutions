class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 값은 늘릴 수만 있으니 목표값은 최댓값이고, 각 원소를 최댓값까지 올리는 횟수의 합 = 최댓값 * n - 전체 합이다
        # 시간 복잡도: O(n)
        return max(nums) * len(nums) - sum(nums)
