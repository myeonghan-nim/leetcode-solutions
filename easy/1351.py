class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        for r in range(rows):
            for c in range(cols - 1, -1, -1):
                if grid[r][c] < 0:
                    count += 1
                else:
                    break

        return count
