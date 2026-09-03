class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 모든 값을 x 단위로만 바꿀 수 있으므로 x로 나눈 나머지가 같아야 한다. 절댓값 차이의 합을 최소로 하는 목표값은 중앙값이다
        # 시간 복잡도: O(m·n log(m·n))
        flat = sorted(v for row in grid for v in row)
        median = flat[len(flat) // 2]
        if any((num - median) % x != 0 for num in flat):
            return -1
        return sum(abs(num - median) // x for num in flat)
