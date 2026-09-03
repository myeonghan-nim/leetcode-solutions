class Solution:
    def climbStairs(self, n: int) -> int:
        # n번째 계단에 오는 방법 = (n-1)번째 + (n-2)번째, 즉 피보나치. 마지막 두 값만 유지한다
        # 시간 복잡도: O(n)
        if n < 3:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
