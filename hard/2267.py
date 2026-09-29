class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        length = m + n - 1

        if length % 2 == 1 or grid[0][0] == ")" or grid[-1][-1] == "(":
            return False

        transposed = m < n
        rows, cols = (n, m) if transposed else (m, n)

        dp = [0] * cols
        dp[0] = 1
        for r in range(rows):
            for c in range(cols):
                states = dp[c]
                if c > 0:
                    states |= dp[c - 1]

                char = grid[c][r] if transposed else grid[r][c]
                if char == "(":
                    states <<= 1
                else:
                    states >>= 1

                remaining = rows + cols - 2 - r - c
                dp[c] = states & ((1 << (remaining + 1)) - 1)

        return bool(dp[-1] & 1)
