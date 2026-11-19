class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        lo1 = lo2 = lo3 = float("inf")
        hi1 = hi2 = hi3 = float("-inf")

        for x in nums:
            if x <= lo1:
                lo1, lo2, lo3 = x, lo1, lo2
            elif x <= lo2:
                lo2, lo3 = x, lo2
            elif x < lo3:
                lo3 = x

            if x >= hi1:
                hi1, hi2, hi3 = x, hi1, hi2
            elif x >= hi2:
                hi2, hi3 = x, hi2
            elif x > hi3:
                hi3 = x

        return min(hi1 - lo3, hi2 - lo2, hi3 - lo1)
