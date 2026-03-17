class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]

            heights = sorted(matrix[i], reverse=True)
            for width, height in enumerate(heights, 1):
                res = max(res, width * height)

        return res
