class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n < 1:
            return False

        count = [0] * (n + 1)

        for num in nums:
            if num < 1 or num > n:
                return False
            count[num] += 1

        for value in range(1, n):
            if count[value] != 1:
                return False

        return count[n] == 2
