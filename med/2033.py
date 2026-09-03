class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = sorted(v for row in grid for v in row)
        median = flat[len(flat) // 2]
        if any((num - median) % x != 0 for num in flat):
            return -1
        return sum(abs(num - median) // x for num in flat)
