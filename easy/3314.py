class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n & 1 == 0:
                ans.append(-1)
                continue

            trailing_ones = 0
            tmp = n
            while tmp & 1:
                trailing_ones += 1
                tmp >>= 1

            ans.append(n - (1 << (trailing_ones - 1)))
        return ans
