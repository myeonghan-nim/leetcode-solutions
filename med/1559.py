class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # 같은 문자끼리 이어진 칸을 DFS로 돌며, 직전 칸이 아닌데 이미 방문한 칸을 다시 만나면 길이 4 이상의 순환이 있다는 뜻이다
        # 시간 복잡도: O(m·n)
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, pi: int, pj: int) -> bool:
            if visited[i][j]:
                return True

            visited[i][j] = True
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j] and (ni != pi or nj != pj):  # 바로 직전 칸으로 되돌아가는 것은 순환이 아니다
                    if dfs(ni, nj, i, j):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and dfs(i, j, -1, -1):
                    return True

        return False
