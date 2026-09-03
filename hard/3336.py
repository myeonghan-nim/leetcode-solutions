from collections import defaultdict
from math import gcd
from typing import List

MOD = 10**9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        # dp[(g1, g2)] = 두 부분 수열의 gcd가 각각 g1, g2인 경우의 수. 각 원소를 안 쓰거나, 첫 번째에 넣거나, 두 번째에 넣는 세 가지로 갱신한다
        # 시간 복잡도: O(n · D^2) — D는 서로 다른 gcd 값의 수
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
