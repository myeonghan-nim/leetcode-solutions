class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 전치(행↔열) 후 각 행을 뒤집으면 시계 방향 90도 회전이 된다
        # 시간 복잡도: O(n^2)
        n = len(matrix)

        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()
