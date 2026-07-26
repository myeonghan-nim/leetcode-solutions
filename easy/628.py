from heapq import nlargest, nsmallest


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        top3 = nlargest(3, nums)
        low2 = nsmallest(2, nums)
        return max(top3[0] * top3[1] * top3[2], top3[0] * low2[0] * low2[1])
