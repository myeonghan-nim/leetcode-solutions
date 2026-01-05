class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs_value = float('inf')
        negative_count = total_sum = 0
        for row in matrix:
            for v in row:
                abs_value = abs(v)
                total_sum += abs_value
                min_abs_value = min(min_abs_value, abs_value)
                if v < 0:
                    negative_count += 1

        if negative_count % 2:
            total_sum -= 2 * min_abs_value
        return total_sum
