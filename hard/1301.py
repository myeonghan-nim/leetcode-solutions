class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        max_sum = [[-1] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]
        max_sum[n - 1][n - 1] = 0
        count[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X" or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                ways = 0
                for di, dj in ((1, 0), (0, 1), (1, 1)):
                    pi, pj = i + di, j + dj
                    if pi < n and pj < n and max_sum[pi][pj] != -1:
                        if max_sum[pi][pj] > best:
                            best = max_sum[pi][pj]
                            ways = count[pi][pj]
                        elif max_sum[pi][pj] == best:
                            ways += count[pi][pj]

                if best == -1:
                    continue

                value = 0 if board[i][j] == "E" else int(board[i][j])
                max_sum[i][j] = best + value
                count[i][j] = ways % MOD

        if max_sum[0][0] == -1:
            return [0, 0]
        return [max_sum[0][0], count[0][0] % MOD]
