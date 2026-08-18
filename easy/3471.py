from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n, count = len(nums), Counter(nums)
        if k == n:
            return max(nums)

        candidates = nums if k == 1 else (nums[0], nums[-1])
        return max((x for x in candidates if count[x] == 1), default=-1)
