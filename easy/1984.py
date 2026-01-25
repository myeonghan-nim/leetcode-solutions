class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return 0

        min_diff = float('inf')
        nums.sort()
        for i in range(n + 1 - k):
            partial_nums = nums[i:i+k]
            min_diff = min(min_diff, partial_nums[-1] - partial_nums[0])
        return min_diff
