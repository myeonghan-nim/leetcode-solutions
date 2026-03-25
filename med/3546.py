class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = 0
        for row in grid:
            total += sum(row)

        if total % 2:
            return False
        target = total // 2

        col_sum = [0] * n
        top = 0
        for i, row in enumerate(grid):
            row_total = 0
            for j, x in enumerate(row):
                row_total += x
                col_sum[j] += x

            top += row_total
            if i < m - 1 and top == target:
                return True

        left = 0
        for j in range(n - 1):
            left += col_sum[j]
            if left == target:
                return True
            if left > target:
                break

        return False
