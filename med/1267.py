class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # 행별·열별 서버 수를 먼저 세고, 자기 행 또는 자기 열에 서버가 2대 이상인 서버만 센다
        # 시간 복잡도: O(m*n)
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]
        return sum(1 for i, row in enumerate(grid) for j, cell in enumerate(row) if cell and (rows[i] > 1 or cols[j] > 1))
