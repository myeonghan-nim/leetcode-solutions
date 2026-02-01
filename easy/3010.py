class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        second = third = 51
        for i in range(1, len(nums)):
            if nums[i] < second:
                third = second
                second = nums[i]
            elif nums[i] < third:
                third = nums[i]
            if second == third == 1:
                break
        return nums[0] + second + third
