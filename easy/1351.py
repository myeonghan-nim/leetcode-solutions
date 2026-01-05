class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for c in row[::-1]:
                if c < 0:
                    count += 1
                else:
                    break
        return count
