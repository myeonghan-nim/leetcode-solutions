class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        p = 0
        while p < n - 1 and nums[p] < nums[p + 1]:
            p += 1

        q = n - 1
        while q > 0 and nums[q - 1] < nums[q]:
            q -= 1

        return 0 < p < q < n - 1 and all(nums[i] > nums[i + 1] for i in range(p, q))
