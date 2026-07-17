from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_value = max(nums)

        frequency = [0] * (max_value + 1)
        for value in nums:
            frequency[value] += 1

        pair_count = [0] * (max_value + 1)
        for divisor in range(1, max_value + 1):
            divisible_count = 0

            for multiple in range(divisor, max_value + 1, divisor):
                divisible_count += frequency[multiple]

            pair_count[divisor] = divisible_count * (divisible_count - 1) // 2

        for divisor in range(max_value, 0, -1):
            for multiple_gcd in range(divisor * 2, max_value + 1, divisor):
                pair_count[divisor] -= pair_count[multiple_gcd]

        for divisor in range(1, max_value + 1):
            pair_count[divisor] += pair_count[divisor - 1]

        return [bisect_right(pair_count, query) for query in queries]
