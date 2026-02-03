class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 3:
            return False
        elif n == 4:
            return nums[0] < nums[1] > nums[2] < nums[3]

        p = 0
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                p += 1
            else:
                break

        q = n - 1
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                q -= 1
            else:
                break

        for i in range(p, q - 1):
            if nums[i] <= nums[i + 1]:
                return False

        return 0 < p < q < n - 1
