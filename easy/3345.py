from math import prod


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        return next(x for x in range(n, n + 10) if prod(map(int, str(x))) % t == 0)
