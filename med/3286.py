class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # 0-1 BFS. 안전한 칸(0)은 비용 0이라 덱 앞에, 위험한 칸(1)은 비용 1이라 덱 뒤에 넣어 최소 피해 경로를 구한다
        # 시간 복잡도: O(m·n)
        m, n = len(grid), len(grid[0])
        dist = [[m * n] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= next_row < m and 0 <= next_col < n:
                    cost = dist[row][col] + grid[next_row][next_col]
                    if cost < dist[next_row][next_col]:
                        dist[next_row][next_col] = cost
                        if grid[next_row][next_col]:
                            queue.append((next_row, next_col))
                        else:
                            queue.appendleft((next_row, next_col))

        return dist[m - 1][n - 1] < health
