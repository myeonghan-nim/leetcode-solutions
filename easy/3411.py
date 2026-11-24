from math import isqrt


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1 if nums[0] == 1 else 0

        maximum = max(nums)

        spf = list(range(maximum + 1))

        for p in range(2, isqrt(maximum) + 1):
            if spf[p] == p:
                for multiple in range(p * p, maximum + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        last = {}
        left = 0
        answer = 2

        for right, value in enumerate(nums):
            x = value

            while x > 1:
                p = spf[x]

                left = max(left, last.get(p, -1) + 1)
                last[p] = right

                while x % p == 0:
                    x //= p

            answer = max(answer, right - left + 1)

        return answer
