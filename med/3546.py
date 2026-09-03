class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # 위쪽 행들의 합이 정확히 전체의 절반이 되는 가로 절단선이 있거나, 왼쪽 열들의 합이 절반이 되는 세로 절단선이 있으면 된다
        # 시간 복잡도: O(m·n)
        m, n = len(grid), len(grid[0])

        total = sum(map(sum, grid))
        if total % 2:
            return False
        target = total // 2

        col_sum = [0] * n
        top = 0
        for i, row in enumerate(grid):
            row_total = 0
            for j, x in enumerate(row):
                row_total += x
                col_sum[j] += x

            top += row_total
            if i < m - 1 and top == target:
                return True

        left = 0
        for j in range(n - 1):
            left += col_sum[j]
            if left == target:
                return True
            if left > target:  # 값이 모두 양수라 누적합은 계속 커지므로 더 볼 필요 없다
                break

        return False
