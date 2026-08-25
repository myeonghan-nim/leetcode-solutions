class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        m = k
        while m in seen:
            m += k
        return m
