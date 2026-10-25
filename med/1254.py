class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        # 땅(0)마다 스택 DFS로 섬 전체를 물(1)로 메우며, 섬의 칸이 하나라도 테두리에 닿으면 닫힌 섬이 아니고 끝까지 닿지 않으면 닫힌 섬이다
        # 시간 복잡도: O(m·n)
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    continue

                grid[i][j] = 1
                stack = [(i, j)]
                closed = True
                while stack:
                    row, col = stack.pop()
                    if row in (0, m - 1) or col in (0, n - 1):
                        closed = False  # 테두리에 닿아도 섬을 끝까지 메워야 같은 섬을 다시 세지 않는다

                    for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                        if 0 <= next_row < m and 0 <= next_col < n and not grid[next_row][next_col]:
                            grid[next_row][next_col] = 1
                            stack.append((next_row, next_col))

                count += closed

        return count
