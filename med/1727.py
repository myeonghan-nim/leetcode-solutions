class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # 각 칸에 '위로 연속된 1의 개수'를 누적해 히스토그램으로 바꾸고, 열을 마음대로 재배열할 수 있으므로 행마다 높이를 내림차순 정렬해 (너비 × 높이)의 최댓값을 구한다
        # 시간 복잡도: O(m·n log n)
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
