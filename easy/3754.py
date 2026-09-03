class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # 0을 제거한 숫자 문자열을 만들어, 그 정수값에 각 자릿수 합을 곱한다
        # 시간 복잡도: O(log n)
        nonzero = str(n).replace("0", "")
        return int(nonzero) * sum(map(int, nonzero))
