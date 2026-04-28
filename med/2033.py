class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
        flat.sort()
        median = flat[len(flat) // 2]
        if any((num - median) % x != 0 for num in flat):
            return -1
        return sum(abs(num - median) // x for num in flat)
