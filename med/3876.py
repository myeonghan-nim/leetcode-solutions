class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimum = min(nums1)
        all_even = all(x % 2 == 0 for x in nums1)
        return minimum % 2 != 0 or all_even
