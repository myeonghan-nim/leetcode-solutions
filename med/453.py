class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # n-1개를 +1 하는 것은 하나를 -1 하는 것과 같으므로, 모든 원소를 최솟값까지 내리는 데 드는 감소량의 합이 답이다
        # 시간 복잡도: O(n)
        return sum(nums) - min(nums) * len(nums)
