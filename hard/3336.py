from collections import defaultdict
from math import gcd
from typing import List

MOD = 10**9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for x in nums:
            ndp = defaultdict(int)
            for (g1, g2), cnt in dp.items():
                ndp[(g1, g2)] = (ndp[(g1, g2)] + cnt) % MOD
                ndp[(gcd(g1, x), g2)] = (ndp[(gcd(g1, x), g2)] + cnt) % MOD
                ndp[(g1, gcd(g2, x))] = (ndp[(g1, gcd(g2, x))] + cnt) % MOD
            dp = ndp

        return sum(c for (g1, g2), c in dp.items() if g1 == g2 != 0) % MOD
