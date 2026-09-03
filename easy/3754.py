class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nonzero = str(n).replace("0", "")
        return int(nonzero) * sum(map(int, nonzero))
