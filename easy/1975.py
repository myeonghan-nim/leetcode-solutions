class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # 인접한 두 칸의 부호를 동시에 뒤집을 수 있으므로 음수 부호는 자유롭게 옮길 수 있다. 음수 개수가 짝수면 모두 양수로 만들 수 있고, 홀수면 절댓값이 가장 작은 칸 하나만 음수로 남긴다
        # 시간 복잡도: O(m·n)
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
            total_sum -= 2 * min_abs_value  # 더해 뒀던 값을 빼는 셈이므로 2배를 뺀다
        return total_sum
