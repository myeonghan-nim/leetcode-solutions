from math import prod


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # 자릿수 곱이 t로 나누어 떨어지는 수는 n부터 10개 안에 반드시 있다(일의 자리가 0인 수는 곱이 0). 그 범위만 확인한다
        # 시간 복잡도: O(1)
        return next(x for x in range(n, n + 10) if prod(map(int, str(x))) % t == 0)
